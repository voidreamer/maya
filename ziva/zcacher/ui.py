from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance

from maya import OpenMayaUI as omui
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

import acMayaApi


class ZUI(QDialog, MayaQWidgetBaseMixin):

    def __init__(self,
                 parent=None):
        super(ZUI, self).__init__(parent)

        self._label_cache_name = QLabel("Cache name")
        self._label_cache_start = QLabel("Start")
        self._label_cache_end = QLabel("End")
        self._name = QLineEdit("zCache1")
        self._start_frame = QLineEdit()
        self._end_frame = QLineEdit()
        self._write_button = QPushButton("write cache")
        self._load_button = QPushButton("load cache")
        self._label_result = QLabel(" ")
        self._ziva_caches = QComboBox()

        self._ziva_caches.addItems(
            [zCaches for zCaches in maya.cmds.ls(type='zCache')])

        cache_layout = QFormLayout()

        cache_layout.addRow(self._ziva_caches)
        cache_layout.addRow(self._label_cache_name,
                            self.name)
        cache_layout.addRow(self._label_cache_start,
                            self.startFrame)
        cache_layout.addRow(self._label_cache_end,
                            self.endFrame)
        cache_layout.addRow(self._write_button,
                            self._load_button)
        cache_layout.addRow(self._label_result)

        self.setLayout(cache_layout)

        self._writeButton.clicked.connect(self.savefile)
        self._loadButton.clicked.connect(self.openfile)

    @property
    def end_frame(self):
        return self._end_frame

    @property
    def label_cache_end(self):
        return self._label_cache_end

    @property
    def label_cache_name(self):
        return self._label_cache_name

    @property
    def label_cache_start(self):
        return self._label_cache_start

    @property
    def label_result(self):
        return self._label_result

    @property
    def start_frame(self):
        return self._startFrame
