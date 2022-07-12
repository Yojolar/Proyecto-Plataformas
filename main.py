import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MenuInterfaz import Ui_menu
from inventario import Ui_inventario
from inventarioSub_provedor import Ui_inv2_provedor
from venta import Ui_Venta


class VentanaPrincipal():

    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        # self.app = QtWidgets.QApplication(sys.argv)
        self.Data = QtWidgets.QDialog()
        self.ui = Ui_menu()
        self.ui.setupUi(self.Data)
        self.Data.show()
        self.ui.pushButton.clicked.connect(self.venta)
        self.ui.pushButton_2.clicked.connect(self.inventario)
        app.exec_()

    def venta(self):
        print("ventas")
        # VentanaVenta()

    def inventario(self):
        print("inventario")
        # VentanaInventario().Data.show()


class prueba():
    def __init__(self):
        print('inicio bien')


class VentanaVenta():

    def __init__(self):
        # self.close()
        super(VentanaVenta, self).__init__()
        self.Data = QtWidgets.QDialog()
        self.ui = Ui_Venta()
        self.ui.setupUi(self.Data)
        self.Data.show()
        app.exec_()


class VentanaInventario():

    def __init__(self):
        super(VentanaInventario, self).__init__()
        # app = QtWidgets.QApplication(sys.argv)
        self.Data = QtWidgets.QDialog()
        self.ui = Ui_inventario()
        self.ui.setupUi(self.Data)
        self.Data.show()
        app.exec_()


class Ui_inv2_provedor():

    def __init__(self):
        super(Ui_inv2_provedor, self).__init__()
        # app = QtWidgets.QApplication(sys.argv)
        self.Data = QtWidgets.QDialog()
        self.ui = Ui_inv2_provedor()
        self.ui.setupUi(self.Data)
        self.Data.show()
        app.exec_()

class VentanaInventarioTercera():

    def __init__(self):
        super(VentanaInventarioTercera, self).__init__()
        # app = QtWidgets.QApplication(sys.argv)
        self.Data = QtWidgets.QDialog()
        self.ui = Ui_inv2_provedor()
        self.ui.setupUi(self.Data)
        self.Data.show()
        app.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    VentanaPrincipal()
    VentanaVenta()
    VentanaInventario()
    Ui_inv2_provedor()
    VentanaInventarioTercera()
