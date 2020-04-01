import maya.cmds as cmds

class Camera_jump():

    def __init__(oldcam, newcam, selected_object):

        oldcam = cmds.lookThru( q=True )

        if oldcam != newcam:
            oldcam = newcam    
        else:
            oldcam = self.oldcam
    
        cmds.warning("current viewing through: " + oldcam)

        cmds.lookThru( oldcam )
        
        [ selected_object = cmds.ls(sl=1)[0] if not selected_object ]

        cmds.viewFit(cmds.ls(selected_object))


