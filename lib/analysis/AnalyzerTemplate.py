# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnalyzerTemplate.ui'
#
# Created: Sat Sep 11 17:34:52 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 559)
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.loaderDock = QtGui.QDockWidget(MainWindow)
        self.loaderDock.setFeatures(QtGui.QDockWidget.DockWidgetMovable)
        self.loaderDock.setObjectName("loaderDock")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.loaderDock.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.loaderDock)
        self.dataDock = QtGui.QDockWidget(MainWindow)
        self.dataDock.setFeatures(QtGui.QDockWidget.DockWidgetMovable)
        self.dataDock.setObjectName("dataDock")
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.dockWidgetContents_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loadDataBtn = QtGui.QPushButton(self.dockWidgetContents_2)
        self.loadDataBtn.setObjectName("loadDataBtn")
        self.verticalLayout.addWidget(self.loadDataBtn)
        self.loadSequenceBtn = QtGui.QPushButton(self.dockWidgetContents_2)
        self.loadSequenceBtn.setObjectName("loadSequenceBtn")
        self.verticalLayout.addWidget(self.loadSequenceBtn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.recompSelectedBtn = QtGui.QPushButton(self.dockWidgetContents_2)
        self.recompSelectedBtn.setObjectName("recompSelectedBtn")
        self.verticalLayout.addWidget(self.recompSelectedBtn)
        self.recompAllBtn = QtGui.QPushButton(self.dockWidgetContents_2)
        self.recompAllBtn.setObjectName("recompAllBtn")
        self.verticalLayout.addWidget(self.recompAllBtn)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.saveSelectedBtn = QtGui.QPushButton(self.dockWidgetContents_2)
        self.saveSelectedBtn.setObjectName("saveSelectedBtn")
        self.verticalLayout.addWidget(self.saveSelectedBtn)
        self.saveAllBtn = QtGui.QPushButton(self.dockWidgetContents_2)
        self.saveAllBtn.setObjectName("saveAllBtn")
        self.verticalLayout.addWidget(self.saveAllBtn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.dataTree = QtGui.QTreeWidget(self.dockWidgetContents_2)
        self.dataTree.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.dataTree.setObjectName("dataTree")
        self.horizontalLayout.addWidget(self.dataTree)
        self.dataDock.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dataDock)
        self.dockWidget_3 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_3.setFeatures(QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.dockWidgetContents_3)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.dockList = QtGui.QListWidget(self.dockWidgetContents_3)
        self.dockList.setObjectName("dockList")
        self.gridLayout.addWidget(self.dockList, 0, 1, 6, 1)
        self.addOutputBtn = QtGui.QPushButton(self.dockWidgetContents_3)
        self.addOutputBtn.setObjectName("addOutputBtn")
        self.gridLayout.addWidget(self.addOutputBtn, 1, 0, 1, 1)
        self.addPlotBtn = QtGui.QPushButton(self.dockWidgetContents_3)
        self.addPlotBtn.setObjectName("addPlotBtn")
        self.gridLayout.addWidget(self.addPlotBtn, 2, 0, 1, 1)
        self.addCanvasBtn = QtGui.QPushButton(self.dockWidgetContents_3)
        self.addCanvasBtn.setObjectName("addCanvasBtn")
        self.gridLayout.addWidget(self.addCanvasBtn, 3, 0, 1, 1)
        self.addTableBtn = QtGui.QPushButton(self.dockWidgetContents_3)
        self.addTableBtn.setObjectName("addTableBtn")
        self.gridLayout.addWidget(self.addTableBtn, 4, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 46, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 0, 2, 1)
        self.removeDockBtn = QtGui.QPushButton(self.dockWidgetContents_3)
        self.removeDockBtn.setObjectName("removeDockBtn")
        self.gridLayout.addWidget(self.removeDockBtn, 6, 1, 1, 1)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget_3)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.loaderDock.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Loader", None, QtGui.QApplication.UnicodeUTF8))
        self.dataDock.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.loadDataBtn.setText(QtGui.QApplication.translate("MainWindow", "Load Data", None, QtGui.QApplication.UnicodeUTF8))
        self.loadSequenceBtn.setText(QtGui.QApplication.translate("MainWindow", "Load Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.recompSelectedBtn.setText(QtGui.QApplication.translate("MainWindow", "Recompute Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.recompAllBtn.setText(QtGui.QApplication.translate("MainWindow", "Recompute All", None, QtGui.QApplication.UnicodeUTF8))
        self.saveSelectedBtn.setText(QtGui.QApplication.translate("MainWindow", "Save Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAllBtn.setText(QtGui.QApplication.translate("MainWindow", "Save All", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_3.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Components", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Add:", None, QtGui.QApplication.UnicodeUTF8))
        self.addOutputBtn.setText(QtGui.QApplication.translate("MainWindow", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.addPlotBtn.setText(QtGui.QApplication.translate("MainWindow", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.addCanvasBtn.setText(QtGui.QApplication.translate("MainWindow", "Canvas", None, QtGui.QApplication.UnicodeUTF8))
        self.addTableBtn.setText(QtGui.QApplication.translate("MainWindow", "Table", None, QtGui.QApplication.UnicodeUTF8))
        self.removeDockBtn.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))

