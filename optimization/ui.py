from __future__ import division
import random
import PySide2.QtWidgets
import PySide2.QtGui
import PySide2.QtCore

import maya.cmds
import maya.api.OpenMaya
import operator
import collections

import utils


class UI(QDialog):

    def __init__(self,
                 parent=None):
        super(UI, self).__init__(parent)
        # Create widgets
        self.setWindowTitle("Find objects by size/weight")
        self._edit = PySide2.QtWidgets.QLabel("Percentage")
        self._button = PySide2.QtWidgets.QPushButton("Threshold")
        self._sl = PySide2.QtWidgets.QSlider(Qt.Horizontal)
        self._leftList = PySide2.QtWidgets.QListWidget()
        self._rightList = PySide2.QtWidgets.QListWidget()
        self._sl.setMinimum(10)
        self._sl.setMaximum(100)
        self._sl.setValue(50)
        self._sl.setTickPosition(QSlider.TicksBelow)
        self._sl.setTickInterval(5)
        # Create layout and add widgets
        mainLayout = PySide2.QtWidgets.QHBoxLayout()
        mainLayout.addWidget(self.leftList)
        layout = PySide2.QtWidgets.QVBoxLayout()
        layout.addWidget(self.rightList)
        layout.addWidget(self.sl)
        layout.addWidget(self.button)
        # Set dialog layout
        mainLayout.addLayout(layout)
        self.setLayout(mainLayout)
        # Add button signal
        self.button.clicked.connect(self.populate_items)
        self.leftList.itemClicked.connect(self.select)

        objects = maya.cmds.ls(type='mesh')
        dic = utils.Utils.get_object_size(objects)
        sorted_objects = sorted(dic.items(), key=operator.itemgetter(1))
        sorted_dict = collections.OrderedDict(sorted_objects)
        self.items = sorted_dict

    def select(self):
        current_item = self.leftList.currentItem()
        maya.cmds.select(current_item.text())
        self.rightList.clear()
        self.rightList.addItem(self.items.get(current_item.text()).__str__())

    def populate_items(self):
        self.leftList.addItems(self.items.keys())



