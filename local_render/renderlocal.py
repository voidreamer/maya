
#!/usr/bin/env python
#----------------------------------------------------------------------------#
#------------------------------------------------------------------ HEADER --#

"""
@author:
    acportillo

@description:
    render locally selected views

@applications:
    - groom
    - cfx
    - fur
"""


import maya.cmds as cmds
import maya.mel as mel
from pymel.core import *
import functools
import os

template = uiTemplate('templ', force=True)
template.define(button, width=100, height=40, align='left')
template.define(frameLayout, borderVisible=True, labelVisible=False)


def showUI():
        
    with window("mainWin", t="Render locally", menuBar=True, menuBarVisible=True) as win:               
        with template:
            with columnLayout( rowSpacing=5 ):
                with frameLayout():
                    text(label = " Asset name ", w=200)
                    textField("tf_assetName", text = cmds.getAttr("master.asset_name"))  
                    
                    text(label = " Version number ", w=200)
                    textField("tf_version", text = "01")  
                    
                with frameLayout( enable=True):
                    with columnLayout():
                        text(label = " Views to render ", w=200)
                        
                        checkBox("vw_front", label='Front', v=1)
                        checkBox("vw_back", label='Back', v=1)
                        checkBox("vw_left", label='Left', v=1)
                        checkBox("vw_right", label='Right', v=1)
                        checkBox("vw_r34", label='right34', v=1)
                        checkBox("vw_l34", label='left34', v=1) 
                                       
                        
                with frameLayout():
                    text(label = " path = ", w=200)                    
                    textField("tf_path", ed = 0, w=200)
                    with columnLayout():
                        button(label='Render', bgc= [0.5,0.2,0.2], w=200, c=ren )
                        

def start():
    if (cmds.window("mainWin", exists=True)):
        cmds.deleteUI("mainWin")
        
    if not (objExists("master")):            
        return    
     
    showUI()
    

def ren(*args): 

    # Output file naming    
    
    if textField( "tf_version", query=True, exists=True ):
        
        version    = textField( "tf_version", query=True, text=False )    
        
    if textField( "tf_assetName", query=True, exists=True ):
        
        assetName  = textField( "tf_assetName", query=True, text=False ) 
            
    cmds.setAttr("defaultRenderGlobals.modifyExtension",0)
    cmds.setAttr("defaultRenderGlobals.imageFilePrefix", "%s/v%s/%s" % (assetName, version, assetName), type="string")
    cmds.setAttr("defaultRenderGlobals.startFrame", 1 )
    cmds.setAttr("defaultRenderGlobals.animation",True)
    cmds.setAttr("defaultRenderGlobals.putFrameBeforeExt",1)
   
    
    # Temporary group for posing asset
    
    views = [0,45,90,180,270,315]   
    
    
    if (objExists("parent_GRP")):
        cmds.delete("parent_GRP")
    grp = cmds.group(em=1, n="parent_GRP")
    
    if (objExists("master")):
        mstr = cmds.ls("master")          
        cmds.parentConstraint(grp, mstr)
    else:
        return

    # Check what views are unchecked and remove them from render line
    
    if not checkBox("vw_front",q=1,v=1):        
        views.remove(0)
    if not checkBox("vw_back",q=1,v=1):
        views.remove(180)
    if not checkBox("vw_left",q=1,v=1):
        views.remove(270)
    if not checkBox("vw_right",q=1,v=1):
        views.remove(90)
    if not checkBox("vw_r34",q=1,v=1):
        views.remove(45)
    if not checkBox("vw_l34",q=1,v=1):
        views.remove(315)
      
    # Gets the path and puts it into the textfield
    
    if textField("tf_path", query = True, exists=True , w=200):
        renpath = cmds.renderSettings(fin=1, fp=1)
        tmppath = renpath[0].replace("images", "images/tmp")        
        
        if len(views) > 0:
            rpath = tmppath.strip(tmppath.split("/")[-1])
        else:
            rpath = "Please select at least a view to render"                               
        
        textField("tf_path", edit=True, text = rpath , w=200)
     
    # Sets the posing keys
    
    for i in range(len(views)):
        ctime = cmds.currentTime(i+1)
        cmds.setAttr("parent_GRP.rotateY", views[i])
        cmds.setKeyframe("parent_GRP.ry")        
        mel.eval('currentTime %s ;' % str(ctime))
        mel.eval('renderWindowRender redoPreviousRender renderView;')
        
    # Tries to call RV with the rendered sequence
        
    try:
        os.system("rv "+rpath+"*.exr")
    except:
        print("An exception occurred")        
    
        
    if (objExists("parent_GRP")):
        cmds.delete("parent_GRP")     
