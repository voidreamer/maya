import maya.OpenMaya
import maya.cmds
import maya.mel
import ui
from ui import ZUI


class ZivaCacher:

    def save_file(self):
        directory = ui.QFileDialog.getExistingDirectory(
            self,
            "Select Directory",
            "~",
            ui.QFileDialog.ShowDirsOnly | ui.QFileDialog.DontResolveSymlinks)

        if directory:

            start_frame = int(ui.ZUI.start_frame.text())
            end_frame = int(ui.ZUI.end_frame.text())
            name = self.name.text()
            currentCache = self.zivaCaches.currentText()

            maya.mel.eval("zCache -clear " + currentCache)
            for i in xrange(start_frame, end_frame):
                maya.cmds.currentTime(i)
                path = dir + '/' + name + '.%04i.zCache' % i
                print path + " written to disk"
                maya.mel.eval('zCache -save "{}" {}'.format(path, currentCache))
                maya.mel.eval("zCache -clear " + currentCache)

            self.lResult.setText(" ... SAVE SUCCESSFUL ... ")

    def open_file(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory", "~",
                                               QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        if directory:
            sf = int(self.startFrame.text())
            ef = int(self.endFrame.text())
            nm = self.name.text()
            currentCache = self.zivaCaches.currentText()

            maya.cmds.currentTime(sf)

            for i in xrange(sf, ef):
                path = directory + '/' + nm + '.%04i.zCache' % i
                print path + " loaded"
                maya.mel.eval('zCache -load "{}" {}'.format(path, currentCache))

            ZUI.label_result.setText(" ... LOAD SUCCESSFUL ... ")


if __name__ == '__main__':
    app = ui.QApplication.instance()
    # Create and show the form
    form = ZUI()
    form.show()
