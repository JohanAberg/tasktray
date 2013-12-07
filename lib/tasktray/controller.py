import sys
from job_widget import Ui_Form
from manifest import QtCore
from manifest import QtGui
__author__ = 'aberg'


class JobWidget(QtGui.QWidget, Ui_Form):
    def __init__(self):
        super(JobWidget, self).__init__()
        self.setupUi(self)

class View(QtGui.QWidget):
    def __init__(self):
        super(View, self).__init__()
        self.setWindowFlags(QtCore.Qt.Popup)
        # self.setWindowFlags(QtCore.Qt.Drawer)
        self.tree = QtGui.QTreeWidget()
        self.tree.setHeaderLabel('Job')
        self.tree.setHeaderHidden(True)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.tree)
        self.setLayout(layout)


    def update_tree(self, tokens):
        for token in tokens:
            item = QtGui.QTreeWidgetItem()
            item.setChildIndicatorPolicy(QtGui.QTreeWidgetItem.ShowIndicator)

            layer_item = QtGui.QTreeWidgetItem(['Comp-Write1'])
            for frame in range(1,36):
                layer_item.addChild(QtGui.QTreeWidgetItem(['%d' % frame]))

            item.addChild(layer_item)
            self.tree.addTopLevelItem(item)
            self.tree.setItemWidget(item, 0, JobWidget())


class Controller(QtCore.QObject):

    def __init__(self):
        super(Controller, self).__init__()
        self.view = View()

        self.view.resize(640, 480)
        self.view.setWindowTitle('Job Widget')

        tokens = ['one', 'two', 'three', 'four']
        self.view.update_tree(tokens)


class SystemTrayIcon(QtGui.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtGui.QSystemTrayIcon.__init__(self, icon, parent)

        self.menu = QtGui.QMenu(parent)
        exitAction = self.menu.addAction("Exit")
        exitAction.triggered.connect(sys.exit)
        self.setContextMenu(self.menu)

        self.activated.connect(self.on_clicked)
        self.con = None

    def on_clicked(self):
        if self.con is None:
            self.con = Controller()
            self.con.view.show()
        else:
            self.con.view.close()
            self.con = None


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    style = app.style()
    w = QtGui.QWidget()
    icon = QtGui.QIcon(style.standardPixmap(QtGui.QStyle.SP_ComputerIcon))
    trayIcon = SystemTrayIcon(icon, w)
    trayIcon.show()

    app.exec_()