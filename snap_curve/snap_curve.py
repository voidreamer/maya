#snapcurve
import maya.cmds as cmds
cmds.delete(cmds.pointConstraint(cmds.ls(sl=1)[1], cmds.ls(sl=1)[0]))
cmds.hide(cmds.ls(sl=1)[1])
