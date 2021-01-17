'''
@author: Alejandro Cabrera <voidreamer@gmail.com>
Utilities to quantify polygonal elements.
'''

import maya.cmds
import maya.api.OpenMaya

import acMayaApi


class Utils(object):

    def __init__(self):
        super(Utils, self).__init__()
        return

    @classmethod
    def get_object_size(cls,
                        object_list):
        """
        :param object_list:
        :return: dict
        """
        objects = {}

        for _object in object_list:
            objects.update({_object: [cls.element_by_number_triangles(_object),
                                      cls.element_by_size(_object)]})
        return objects

    @staticmethod
    def get_distance(bounding_box):
        """
        :param bounding_box:
        :return: float
        """
        point1 = maya.api.OpenMaya.MPoint(bounding_box[0],
                                          bounding_box[1],
                                          bounding_box[2])

        point2 = maya.api.OpenMaya.MPoint(bounding_box[3],
                                          bounding_box[4],
                                          bounding_box[5])

        return point1.distanceTo(point2)

    @classmethod
    def element_by_size(cls,
                        obj):
        """
        :param obj:
        :return: float
        """
        mesh_bbox = maya.cmds.exactWorldBoundingBox(obj)
        return cls.get_distance(mesh_bbox)

    @staticmethod
    def element_by_number_triangles(obj):
        """
        :param obj:
        :return: float
        """
        return maya.cmds.polyEvaluate(obj,
                                      t=True)
