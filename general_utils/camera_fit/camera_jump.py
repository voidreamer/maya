import maya.cmds as cmds
import acMayaApi

## Deprecated
#TODO
class CameraJump:

    def __init__(self, oldcam, newcam, selected_object):

        camera_node = acMayaApi.node.ACNode('camera1')

        for camera_child in camera_node.connections():
            print camera_child

        oldcam = cmds.lookThru(q=True)

        if oldcam != newcam:
            oldcam = newcam
        else:
            oldcam = self.oldcam

        cmds.warning("current viewing through: " + oldcam)

        cmds.lookThru(oldcam)

        if selected_object is not None:
            selected_object = cmds.ls(sl=1)[0]

        cmds.viewFit(cmds.ls(selected_object))
