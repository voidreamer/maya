'''
@author: Alejandro Cabrera <voidreamer@gmail.com>
Main module to represent any node in the Maya API.
'''

import maya.OpenMaya
import maya.api.OpenMaya
import maya.cmds

import acMayaApi


class ACNode(maya.OpenMaya.MObject):
    """Node representing any maya object in the scene."""

    def __init__(self,
                 in_node):
        super(ACNode, self).__init__(in_node)

        return

    def add_attribute(self,
                      in_attribute):
        """Add an attribute to specified node.

        :param in_attribute: (maya.OpenMaya.MObject)
        :return: None
        """
        dependency = self.dependency_node
        attribute = maya.OpenMaya.MFnAttribute()
        attribute.setObject(in_attribute)

        if dependency.hasAttribute(attribute.name()):
            # The node already has the attribute
            raise NotImplementedError

        dependency.addAttribute(in_attribute)

        return

    @property
    def dependency_node(self):
        if not self.hasFn(maya.OpenMaya.MFn.kDependencyNode):
            raise NotImplementedError

        return maya.OpenMaya.MFnDependencyNode(self)

    @property
    def children(self):

        path = self.mDagPath
        if path is None:
            return

        for index in xrange(path.child_count()):
            node = path.child(index)
            if node.hasFn(maya.OpenMaya.MFn.kTransform):
                yield self.BASE_CLASS(node)

    @property
    def connections(self):
        dependency = self.dependency_node
        connections = maya.OpenMaya.MPlugArray()
        try:
            dependency.getConnections(connections)
        except:
            raise StopIteration

        plug_type = self.__plugType
        for index in xrange(connections.length()):
            yield plug_type(connections[index])

    def create_attribute(self,
                         in_name,
                         in_value,
                         in_default_value,
                         in_type):

        dependency = self.dependency_node
        if dependency.hasAttribute(in_name):
            # object already has the attribute
            raise NotImplementedError

        if in_type is None:
            if in_value is not None:
                value = in_value
            if in_default_value is not None:
                value = in_default_value
            else:
                # Missing argument (type)
                raise NotImplementedError

            value_type = self.get_attribute_by_type(value)
        else:
            value_type = in_type

        if value_type < 0:
            if in_default_value is None:
                args = ()
            else:
                args = (in_default_value,)

            if value_type == acMayaApi.constants.VALUE_TYPE_MATRIX:
                attribute = maya.OpenMaya.MFnMatrixAttribute()
            else:
                attribute = maya.OpenMaya.MFnTypedAttribute()

            attribute_obj = attribute.create(in_name,
                                             -value_type,
                                             *args)

        elif value_type == acMayaApi.constants.VALUE_TYPE_ENUM:
            attribute = maya.OpenMaya.MFnEnumAttribute()
            attribute_obj = attribute.create(in_name,
                                             in_default_value)

        dependency.addAttribute(attribute_obj)

    def delete(self):
        maya.cmds.delete(self.full_name)

    @property
    def full_name(self):
        path = self.m_dag_path
        if path is None:
            return self.dependency_node.name()
        return path.full_path_name()

    @property
    def m_dag_path(self):
        return maya.OpenMaya.MDagPath(self.path)
