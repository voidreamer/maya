'''
@author: Alejandro Cabrera
'''

import maya.cmds
import acMayaApi


def duplicate_and_blend_curves(in_curves,
                               blend=False):
    input_curves = in_curves
    try:
        in_curves_node = acMayaApi.node.ACNode(input_curves)
    except:
        raise NotImplementedError

    if input_curves is not None:
        control_group = maya.cmds.group(name='control_curves_GRP',
                                        empty=True)
        try:
            in_children = in_curves_node.children
        except:
            raise NotImplementedError

        for input_curve in input_curves:
            blend_curve = maya.cmds.duplicate(input_curve,
                                              name='icurve#')
            maya.cmds.parent(blend_curve,
                             control_group)

            if blend:
                maya.cmds.blendShape(blend_curve,
                                     input_curve,
                                     weight=(0, 1))


if __name__ == "__main__":
    curves = maya.cmds.ls(dag=True,
                          allPaths=True,
                          selection=True,
                          type='nurbsCurve')
    duplicate_and_blend_curves(curves, True)
