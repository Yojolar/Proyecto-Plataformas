from PyQt5 import uic, QtWidgets
from Funciones_DB import buscar_proveedores, buscar_todos_productos
from Funciones_DB import agregar_producto_proveedor
from pop_up_error import Pop_up
from ventana_nuevo_producto import Nuevo_producto
from ventana_nuevo_proveedor import Nuevo_proveedor
qtCreatorFile = 'invSub_modificarProducto.ui'

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class Agregar_Productos(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        listaProductos = self.actualizar_lista('prod')
        listaProveedores = self.actualizar_lista('proveed')
        self.editProd_box_productoStock.addItems(listaProductos)
        self.editProd_box_proveedorStock.addItems(listaProveedores)
        self.editProd_button_addProducto.clicked.connect(self.agregar_cantidad)
        self.editProd_button_newProducto.clicked.connect(self.nuevo_producto)
        self.editProd_button_newProveedor.clicked.connect(self.nuevo_proveedor)
        self.editProd_button_addProducto_2.clicked.connect(self.actualizar)
        self.editProd_button_regresar.clicked.connect(self.regresar)

    def regresar(self):
        print("regresando")
        self.close()

    def actualizar(self):
        self.editProd_box_productoStock.clear()
        self.editProd_box_proveedorStock.clear()
        listaProductos = self.actualizar_lista('prod')
        listaProveedores = self.actualizar_lista('proveed')
        self.editProd_box_productoStock.addItems(listaProductos)
        self.editProd_box_proveedorStock.addItems(listaProveedores)

    def actualizar_lista(self, var):
        if var == 'prod':
            lista = buscar_todos_productos()
            self.editProd_box_productoStock.insertItem(0, '')
        if var == 'proveed':
            lista = buscar_proveedores()
            self.editProd_box_proveedorStock.insertItem(0, '')
        return lista

    def agregar_cantidad(self):
        producto = self.editProd_box_productoStock.currentText()
        proveedor = self.editProd_box_proveedorStock.currentText()
        cantidad = self.editProd_text_cantidad.toPlainText()
        procesada = ''.join(cantidad.split())
        if procesada == '' or proveedor == '' or producto == '':
            self.pop = Pop_up()
            self.pop.show()
        elif procesada.isdigit() is False:
            self.pop = Pop_up()
            self.pop.show()
        elif int(procesada) < 0:
            self.pop = Pop_up()
            self.pop.show()
        else:
            agregar = [producto, int(procesada),  proveedor]
            agregar_producto_proveedor(agregar)
            self.editProd_box_productoStock.clear()
            self.editProd_box_proveedorStock.clear()
            self.editProd_text_cantidad.clear()

    def nuevo_proveedor(self):
        self.prov = Nuevo_proveedor()
        self.prov.show()

    def nuevo_producto(self):
        self.prod = Nuevo_producto()
        self.prod.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Agregar_Productos()
    window.show()
    sys.exit(app.exec_())
