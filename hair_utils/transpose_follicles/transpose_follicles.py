"""
@author:
    Alejandro Cabrera

@description:
    transpose selected follicles.

"""

import maya.cmds
import acMayaApi


def transpose_follicles(in_source,
                        in_destination):

    in_mesh = in_source + ".outMesh"
    out_mesh = in_destination+".outMesh"

    out_mesh_plug = maya.cmds.listConnections(out_mesh, p=1)
    world_matrix0_plug = maya.cmds.listConnections(
        in_source+".worldMatrix[0]", p=1)

    for connection in out_mesh_plug:
        maya.cmds.disconnectAttr(in_mesh, connection)
        maya.cmds.connectAttr(out_mesh, connection)

    for connection2 in world_matrix0_plug:
        maya.cmds.disconnectAttr(in_source+".worldMatrix[0]", connection2)
        maya.cmds.connectAttr(in_destination+".worldMatrix[0]", connection2)

    return


if __name__ == "__main__":
    if maya.cmds.objectType(object) != "mesh":
        maya.cmds.warning("invalid selection, select two meshes, origin and source")
    else:
        old_mesh = maya.cmds.listRelatives(maya.cmds.ls(sl=1)[0])[0]
        new_mesh = maya.cmds.listRelatives(maya.cmds.ls(sl=1)[1])[0]

        transpose_follicles(old_mesh,
                            new_mesh)



