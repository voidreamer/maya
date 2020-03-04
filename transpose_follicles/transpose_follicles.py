import maya.cmds as cmds

oldmesh = cmds.listRelatives(cmds.ls(sl=1)[0])[0]
newmesh = cmds.listRelatives(cmds.ls(sl=1)[1])[0]

con_outm = cmds.listConnections(oldmesh+".outMesh", p=1)
con_mtrx = cmds.listConnections(oldmesh+".worldMatrix[0]", p=1)

for connection in con_outm:
    cmds.disconnectAttr(oldmesh+".outMesh", connection)
    cmds.connectAttr(newmesh+".outMesh", connection)
    
for connection2 in con_mtrx:
    cmds.disconnectAttr(oldmesh+".worldMatrix[0]", connection2)
    cmds.connectAttr(newmesh+".worldMatrix[0]", connection2)
