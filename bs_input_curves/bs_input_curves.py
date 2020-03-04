# siggy:siggyDefault_hairA_34_INPUT
import maya.cmds as cmds

# make blendshape 1 to 2
crv_sel = ""
crv_sel = cmds.ls(sl=1, long=1)[0]
crv_name = crv_sel.split("|")[-1]
input_crv = cmds.ls(crv_name.replace("siggy:", "siggy:cache:"))
cmds.select(input_crv)

cmds.blendShape(input_crv, crv_sel)
