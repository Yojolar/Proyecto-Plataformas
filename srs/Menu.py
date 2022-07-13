from PyQt5 import uic, QtWidgets
from ventana_venta import Venta
from Ventana_agregar_cantidad import Agregar_Productos
from inventario import Inventario
qtCreatorFile = 'MenuInterfaz.ui'

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class Menu(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.abrirVenta)
        self.pushButton_2.clicked.connect(self.abrirInventario)

    def abrirVenta(self):
        self.venta = Venta()
        self.venta.show()

    def abrirInventario(self):
        self.inventario = Inventario()
        self.inventario.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Menu()
    window.show()
    sys.exit(app.exec_())
