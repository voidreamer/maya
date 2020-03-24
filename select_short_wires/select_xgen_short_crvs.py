"""
@author:
    Alejandro Cabrera

@description:
    select short curves from animwires warning dialog [ XGEN ]

"""


import maya.cmds as cmds
import os
import pymel.core as pymel


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
    split_text = texto.replace("Shape.", "Shape").split(" ")
    cmds.select(cl=1)
    for t in split_text:
        if "Shape" in t:
            cmds.select(t, add=1)

