from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance

from maya import OpenMayaUI as omui 
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

import sys
import os
import functools

import maya.cmds as cmds
import maya.mel as mm
import maya.standalone


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # widgets
        self.lCacheName = QLabel("Cache name")
        self.lCacheStart = QLabel("Start")
        self.lCacheEnd = QLabel("End")
        self.name = QLineEdit("zCache1")        
        self.startFrame = QLineEdit("89")
        self.endFrame = QLineEdit("200")
        self.writeButton = QPushButton("write cache")
        self.loadButton = QPushButton("load cache")
        self.lResult = QLabel(" ")
        
        self.zivaCaches = QComboBox()

        self.zivaCaches.addItems([zCaches for zCaches in cmds.ls(type = 'zCache')])
        
        str(cmds.getAttr('rayburn:muscle_zSolver.startFrame'))

        mainlayout = QFormLayout()
        layout = QFormLayout()      
        layout2 = QFormLayout()   
        
        layout.addRow(self.zivaCaches)
        layout.addRow(self.lCacheName, self.name )
        layout.addRow(self.lCacheStart, self.startFrame)
        layout.addRow(self.lCacheEnd, self.endFrame)
        layout.addRow(self.writeButton, self.loadButton)
        layout.addRow(self.lResult)
       
        # Set dialog layout
        self.setLayout(layout)      
        
        self.writeButton.clicked.connect(self.savefile)
        self.loadButton.clicked.connect(self.openfile)
        
        
    def savefile(self):
        dir = QFileDialog.getExistingDirectory(self, "Select Directory", "~", QFileDialog.ShowDirsOnly| QFileDialog.DontResolveSymlinks)  
        if dir:            
            start_frame = int(self.startFrame.text())
            end_frame = int(self.endFrame.text())
            name = self.name.text()
            currentCache = self.zivaCaches.currentText()
            
            mm.eval("zCache -clear "+currentCache )
            for i in xrange( start_frame, end_frame ): 
                cmds.currentTime( i )
                path = dir+'/'+name+'.%04i.zCache' % i
                print path+" written to disk"
                mm.eval('zCache -save "{}" {}'.format(path, currentCache ))   
                mm.eval("zCache -clear "+currentCache )             
                
            self.lResult.setText(" ... SAVE SUCCESSFUL ... ")
        
    def openfile(self):
        dir = QFileDialog.getExistingDirectory(self, "Select Directory", "~", QFileDialog.ShowDirsOnly| QFileDialog.DontResolveSymlinks)
        if dir:
            sf = int(self.startFrame.text())
            ef = int(self.endFrame.text())
            nm = self.name.text()
            currentCache = self.zivaCaches.currentText()
            
            cmds.currentTime( sf )
            
            for i in xrange( sf,ef ):                 
                path = dir+'/'+nm+'.%04i.zCache' % i
                print path+" loaded"                
                mm.eval('zCache -load "{}" {}'.format(path, currentCache ))
         
            self.lResult.setText(" ... LOAD SUCCESSFUL ... ")
    
if __name__ == '__main__':

    # Create the Qt Application
    app = QApplication.instance()
    # Create and show the form
    form = Form()
    form.show()

