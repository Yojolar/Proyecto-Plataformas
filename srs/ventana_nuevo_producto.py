from PyQt5 import uic, QtWidgets
from Funciones_DB import agregar_producto
from pop_up_error import Pop_up
qtCreatorFile = 'invSub_modificarProdSub_variosProductos.ui'
#qtCreatorFile2 = 'venta_pop_Enombre.ui'
qtCreatorFile3 = 'inicio_fake.ui'

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
#Ui_pop, QtBaseClass = uic.loadUiType(qtCreatorFile2)
Ui_fake, QtBaseClass = uic.loadUiType(qtCreatorFile3)


#class Pop_up(QtWidgets.QDialog, Ui_pop):
#    def __init__(self):
#        QtWidgets.QDialog.__init__(self)
#        Ui_pop.__init__(self)
#        self.setupUi(self)


class Inicio_fake(QtWidgets.QDialog, Ui_fake):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_fake.__init__(self)
        self.setupUi(self)


class Nuevo_producto(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.varProd_button_newProducto.clicked.connect(self.agregar)


    def agregar(self):
        producto = self.varProd_text_producto.toPlainText()
        precio = self.varProd_text_precio.toPlainText()
        prod_procesado = ''.join(producto.split())

        if prod_procesado == '':
            self.pop = Pop_up()
            self.pop.show()

        elif precio.isdigit() is False:
            self.pop = Pop_up()
            self.pop.show()
        elif int(precio) < 0:
            self.pop = Pop_up()
            self.pop.show()
        else:
            agregar_producto(producto, int(precio))
            self.varProd_text_producto.clear()
            self.varProd_text_precio.clear()
            print('Se ve bien')
            self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Nuevo_producto()
    window.show()
    sys.exit(app.exec_())
