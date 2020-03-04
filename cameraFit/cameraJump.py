import maya.cmds as cmds

oldcam = cmds.lookThru( q=True )

if oldcam != 'persp':
    oldcam = 'persp'    
else:
    oldcam = cmds.ls("*:*L_stereo*", type='camera')[0]
    
cmds.warning("current viewing through: " + oldcam)

cmds.lookThru( oldcam )
sel = cmds.ls(sl=1)[0]
#cmds.viewFit(cmds.ls("*:*body_REN_collider*")[0])
cmds.viewFit(cmds.ls(sel))


