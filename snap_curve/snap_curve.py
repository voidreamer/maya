#snapcurve

import maya.cmds as cmds

class Snap():
    def __init__(self, selection1, selection2, hide = True): 
        cmds.delete(cmds.pointConstraint(selection1, selection2))
        if hide:
            cmds.hide(selection1)
