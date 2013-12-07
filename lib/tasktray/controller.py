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

        self.tree = QtGui.QTreeWidget()
        self.tree.setHeaderLabel('Job')

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.tree)
        self.setLayout(layout)

        # tokens = ['one', 'two', 'three', 'four']
        # self.update_tree(tokens)

    def update_tree(self, tokens):
        for token in tokens:
            item = QtGui.QTreeWidgetItem()
            item.setChildIndicatorPolicy(QtGui.QTreeWidgetItem.ShowIndicator)
            item.addChild(QtGui.QTreeWidgetItem(['Comp-Write1']))
            # item.setText(0, token)
            job_widget = JobWidget()
            self.tree.addTopLevelItem(item)
            self.tree.setItemWidget(item, 0, job_widget)


class Controller(QtCore.QObject):

    def __init__(self):
        super(Controller, self).__init__()
        self.view = View()
        tokens = ['one', 'two', 'three', 'four']
        self.view.update_tree(tokens)
        self.view.resize(640, 480)
        self.view.setWindowTitle('Job Widget')



if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)

    con = Controller()
    #con.view.setWindowFlags(con.view.windowFlags() | QtCore.Qt.FramelessWindowHint)
    con.view.show()

    app.exec_()