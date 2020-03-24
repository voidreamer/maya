## applies blendshapes from selected input curves to export curves

import maya.cmds as cmds

selection = cmds.ls(sl=1)
animwires_selection = cmds.ls(sl=1)

animwires_selection = [ curve.replace("input_crvs", "output_crvs") for curve in selection ]

blendshapes = []

for input_crv, animwire_crv in zip(selection, animwires_selection):
    blendshapes.append ( cmds.blendShape(input_crv, animwire_crv, en=1, w=[(0, 1)], o="world",n="fromInputBS_{0}".format(input_crv.split(":")[-1]))  )

cmds.select([blendshape[0] for blendshape in blendshapes], add=True)