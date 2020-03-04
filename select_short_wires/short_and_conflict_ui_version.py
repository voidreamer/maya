#!/usr/bin/env python
#---------------------------------------#
#----------------------------- HEADER --#
# creates locator on conflicted areas 

import maya.cmds as cmds
import os
import pymel.core as pymel
import re


def load_file():    
    w = cmds.window("debug animwires", w = 150)
    cmds.columnLayout()
    cmds.button("conflict", c="process_text(False)")
    cmds.button("short", c="process_text(True)")
    cmds.showWindow(w)

def process_text(type):
    fle = open("/home/acportillo/private/texto.txt","r")    
    texto = fle.read()
    fle.close()
    if type:
        split_text = texto.replace("Shape.", "Shape").split(" ")
        cmds.select(cl=1)
        for t in split_text:
            if "Shape" in t:
                cmds.select(t, add=1)
    else:        
        split_text = texto.split(" ")
        pos = []
    
        for t in split_text:
            start = t.find('[')
            end = t.find(']')
            s = t[start:end+1]        
            if "[" in t:
                try:
                    pos = [list(float(i) for i in s.strip("[]").split(","))][0]    
                except:
                    print "ok"               
                cmds.spaceLocator(n="debug_", p=pos)
            
load_file()