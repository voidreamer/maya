import maya.cmds
import maya.api.OpenMaya
import PySide2.QtWidgets

import utils
import ui

if __name__ == '__main__':
    # Create the Qt Application
    app = ui.UI.QApplication.instance()
    # Create and show the form
    form = ui.UI()
    form.show()
    form.populate_items()