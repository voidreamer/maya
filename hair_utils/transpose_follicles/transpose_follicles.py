
"""
@author:
    Alejandro Cabrera

@description:
    render locally selected views

"""

import maya.cmds as cmds

class Transpose_follicles():

    def selection:
        oldmesh = cmds.listRelatives(cmds.ls(sl=1)[0])[0]
        newmesh = cmds.listRelatives(cmds.ls(sl=1)[1])[0]

    def __main__:
        if cmds.objectType(object) != "mesh":
            cmds.warning("invalid selection, select two meshes, origin and source")
            return
        else:
            transpose_follicles(oldmesh, newmesh)

    def transpose_follicles(source, destination):    

        con_outm = cmds.listConnections(source+".outMesh", p=1)
        con_mtrx = cmds.listConnections(source+".worldMatrix[0]", p=1)
        
        for connection in con_outm:
            cmds.disconnectAttr(source+".outMesh", connection)
            cmds.connectAttr(destination+".outMesh", connection)
            
        for connection2 in con_mtrx:
            cmds.disconnectAttr(source+".worldMatrix[0]", connection2)
            cmds.connectAttr(destination+".worldMatrix[0]", connection2)
