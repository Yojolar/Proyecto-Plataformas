from PyQt5 import uic,  QtWidgets
from Ventana_agregar_cantidad import Agregar_Productos
from Funciones_DB import *
qtCreatorFile = 'inventario.ui'

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class Inventario(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.inv_button_regresar.clicked.connect(self.regresar)
        self.inv_button_editProducto.clicked.connect(self.venEditProduct)
        self.inv_button_actualizar.clicked.connect(self.actualizar)
        table_data = mostrar_inventario()
        self.inv_tableWidget_inventario.setColumnCount(3)
        self.inv_tableWidget_inventario.setRowCount(len(table_data))
        self.inv_tableWidget_inventario.setHorizontalHeaderLabels(['Producto', 'Cantidad', 'Precio'])
        for i, (Producto, Cantidad, Precio) in enumerate(table_data):
            self.inv_tableWidget_inventario.setItem(i, 0, QtWidgets.QTableWidgetItem(Producto))
            self.inv_tableWidget_inventario.setItem(i, 1, QtWidgets.QTableWidgetItem(str(Cantidad)))
            self.inv_tableWidget_inventario.setItem(i, 2, QtWidgets.QTableWidgetItem(str(Precio)))
        ##################################################################

    def venEditProduct(self):
        self.agregar = Agregar_Productos()
        self.agregar.show()

    def actualizar(self):
        self.inv_tableWidget_inventario.clear()
        table_data = mostrar_inventario()
        self.inv_tableWidget_inventario.setColumnCount(3)
        self.inv_tableWidget_inventario.setRowCount(len(table_data))
        self.inv_tableWidget_inventario.setHorizontalHeaderLabels(['Producto', 'Cantidad', 'Precio'])
        for i, (Producto, Cantidad, Precio) in enumerate(table_data):
            self.inv_tableWidget_inventario.setItem(i, 0, QtWidgets.QTableWidgetItem(Producto))
            self.inv_tableWidget_inventario.setItem(i, 1, QtWidgets.QTableWidgetItem(str(Cantidad)))
            self.inv_tableWidget_inventario.setItem(i, 2, QtWidgets.QTableWidgetItem(str(Precio)))
        ##################################################################

    def regresar(self):
        print("cerrar")
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inventario = Inventario()
    inventario.show()
    sys.exit(app.exec_())
