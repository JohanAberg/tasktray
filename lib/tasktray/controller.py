import sys
from shotpie.model import Model
from shotpie.view import View
from manifest import QtCore
from manifest import QtGui
__author__ = 'aberg'

class Controller(QtCore.QObject):

    def __init__(self):
        super(Controller, self).__init__()
        self.view = View()
        self.view.resize(640, 480)
        self.view.setWindowTitle('ShotPie')
        self.model = Model()
        self.view.setScene(self.model)
        self.model.refresh()
        self.view.fitInView(self.model.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)



if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)

    con = Controller()
    #con.view.setWindowFlags(con.view.windowFlags() | QtCore.Qt.FramelessWindowHint)
    con.view.show()

    app.exec_()