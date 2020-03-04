#!/usr/bin/env python
#----------------------------------------------------------------------------#
#------------------------------------------------------------------ HEADER --#
# creates locator on conflicted areas 

import maya.cmds as cmds
import os
import pymel.core as pymel
import re


def load_file():
    fname = pymel.fileDialog2(dialogStyle=2, fileFilter="All files (*)",
                            caption="Select the text file",
                            fileMode=1, okCaption="Open")

    if not fname: return ## user cancelled
    else: fname = fname[0]    
    
    fle = open(fname,"r")
    texto = fle.read()
    fle.close()
    
    process_text(texto)

def process_text(texto):
    
    split_text = texto.split(" ")
    pos = []

    for t in split_text:
        start = t.find('[')
        end = t.find(']')
        s = t[start:end+1]        
        if "[" in t:
            pos = [list(float(i) for i in s.strip("[]").split(","))][0]                   
            cmds.spaceLocator(p=pos)