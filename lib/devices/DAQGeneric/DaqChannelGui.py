# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4 import Qwt5 as Qwt
import AOChannelTemplate, DOChannelTemplate, InputChannelTemplate
from lib.util.SequenceRunner import *
from lib.util.WidgetGroup import *
import numpy

class DaqChannelGui(QtGui.QWidget):
    def __init__(self, parent, name, config, plot, dev, prot):
        QtGui.QWidget.__init__(self, parent)
        
        ## Name of this channel
        self.name = name
        
        ## Configuration for this channel defined in the device configuration file
        self.config = config
        
        if 'scale' in config:
            self.scale = config['scale']
        else:
            self.scale = 1.0
        #print "device %s scale=%f" % (name, self.scale)
        
        ## The device handle for this channel's DAQGeneric device
        self.dev = dev
        
        ## The protocol GUI window which contains this object
        self.prot = prot
        
        ## Make sure protocol interface includes our DAQ device
        self.daqDev = self.dev.getDAQName(self.name)
        self.daqUI = self.prot.getDevice(self.daqDev)
        
        ## plot widget
        self.plot = plot
        plot.setCanvasBackground(QtGui.QColor(0,0,0))
        plot.plot()
        
        ## Curves displayed in self.plot
        self.plots = []
        
            
    def postUiInit(self):
        ## Automatically locate all read/writable widgets and group them together for easy 
        ## save/restore operations
        self.stateGroup = WidgetGroup(self)
        
        self.displayCheckChanged()
        QtCore.QObject.connect(self.ui.displayCheck, QtCore.SIGNAL('stateChanged(int)'), self.displayCheckChanged)
            
    def saveState(self):
        #print "Requesting DAQ channel state:", self.stateGroup.state()
        return self.stateGroup.state()
    
    def restoreState(self, state):
        self.stateGroup.setState(state)
        if hasattr(self.ui, 'waveGeneratorWidget'):
            self.ui.waveGeneratorWidget.update()

    def clearPlots(self):
        for i in self.plots:
            i.detach()
        self.plots = []

    def displayCheckChanged(self):
        if self.stateGroup.state()['displayCheck']:
            self.plot.show()
        else:
            self.plot.hide()
            
    def protoStarted(self, params):
        pass
        
class OutputChannelGui(DaqChannelGui):
    def __init__(self, *args):
        DaqChannelGui.__init__(self, *args)
        
        self.currentPlot = None
        if self.config['type'] == 'ao':
            self.ui = AOChannelTemplate.Ui_Form()
        elif self.config['type'] == 'do':
            self.ui = DOChannelTemplate.Ui_Form()
        else:
            raise Exception("Unrecognized channel type '%s'" % self.config['type'])
        self.ui.setupUi(self)
        self.postUiInit()
        self.ui.waveGeneratorWidget.setTimeScale(1e-3)
        
        self.daqChanged(self.daqUI.currentState())
        
            

        QtCore.QObject.connect(self.daqUI, QtCore.SIGNAL('changed'), self.daqChanged)
        QtCore.QObject.connect(self.ui.waveGeneratorWidget, QtCore.SIGNAL('changed'), self.updateWaves)

        
    
    def daqChanged(self, state):
        self.rate = state['rate']
        self.numPts = state['numPts']
        self.timeVals = numpy.linspace(0, float(self.numPts)/self.rate, self.numPts)
        self.updateWaves()
        
    def listSequence(self):
        return self.ui.waveGeneratorWidget.listSequences()
    
    def generateProtocol(self, params=None):
        if params is None:
            params = {}
        prot = {}
        state = self.stateGroup.state()
        if state['preSetCheck']:
            prot['preset'] = state['preSetSpin']
        if state['holdingCheck']:
            prot['holding'] = state['holdingSpin']
        if state['functionCheck']:
            prot['command'] = self.scale * self.getSingleWave(params)
            
        #print prot
        return prot
    
    def handleResult(self, result):
        pass
    
    def updateWaves(self):
        self.clearPlots()
        
        ## display sequence waves
        params = {}
        ps = self.ui.waveGeneratorWidget.listSequences()
        for k in ps:
            params[k] = range(ps[k])
        waves = []
        runSequence(lambda p: waves.append(self.getSingleWave(p)), params, params.keys(), passHash=True)
        for w in waves:
            if w is not None:
                self.plotCurve(w, color=QtGui.QColor(100, 100, 100), replot=False)
        
        ## display single-mode wave in red
        single = self.getSingleWave()
        if single is not None:
            self.plotCurve(single, color=QtGui.QColor(200, 100, 100))
        self.emit(QtCore.SIGNAL('sequenceChanged'), self.dev.name)
        
    def protoStarted(self, params):
        ## Draw green trace for current command waveform
        if not self.stateGroup.state()['displayCheck']:
            return
        if self.currentPlot is not None:
            self.currentPlot.detach()
        
        cur = self.getSingleWave(params)
        #cur = self.ui.waveGeneratorWidget.getSingle(self.rate, self.numPts, params)
        if cur is not None:
            self.currentPlot = self.plotCurve(cur, color=QtGui.QColor(100, 200, 100))
        
    def plotCurve(self, data, color=QtGui.QColor(100, 100, 100), replot=True):
        plot = Qwt.QwtPlotCurve('cell')
        plot.setPen(QtGui.QPen(color))
        plot.setData(self.timeVals, data)
        plot.attach(self.plot)
        self.plots.append(plot)
        if replot:
            self.plot.plot()
        return plot

    def getSingleWave(self, params=None):
        ## waveGenerator generates values in mV or pA
        #print "    get wave:", params
        wave = self.ui.waveGeneratorWidget.getSingle(self.rate, self.numPts, params)
        
        if wave is None:
            return None
        state = self.stateGroup.state()
        if state['holdingCheck']:
            wave += (state['holdingSpin'] / self.scale)
        return wave
        
class InputChannelGui(DaqChannelGui):
    def __init__(self, *args):
        DaqChannelGui.__init__(self, *args)
        self.ui = InputChannelTemplate.Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.prot, QtCore.SIGNAL('protocolStarted'), self.clearPlots)
        self.postUiInit()
                
    def listSequence(self):
        return []
    
    def generateProtocol(self, params=None):
        if params is None:
            params = {}
        state = self.stateGroup.state()
        return {'record': state['recordCheck'], 'recordInit': state['recordInitCheck']}
    
    def handleResult(self, result):
        if self.stateGroup.state()['displayCheck']:
            plot = Qwt.QwtPlotCurve('cell')
            plot.setPen(QtGui.QPen(QtGui.QColor(200, 200, 200)))
            plot.setData(result.xvals('Time'), result)
            plot.attach(self.plot)
            self.plots.append(plot)
            self.plot.plot()
    