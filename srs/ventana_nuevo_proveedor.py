from PyQt5 import uic, QtWidgets
from Funciones_DB import ingresar_proveedor
qtCreatorFile = 'invSub_modificarProdSub_newProvedor.ui'
qtCreatorFile2 = 'venta_pop_Enombre.ui'
qtCreatorFile3 = 'inicio_fake.ui'

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
Ui_pop, QtBaseClass = uic.loadUiType(qtCreatorFile2)
Ui_fake, QtBaseClass = uic.loadUiType(qtCreatorFile3)


class Pop_up(QtWidgets.QDialog, Ui_pop):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_pop.__init__(self)
        self.setupUi(self)


class Inicio_fake(QtWidgets.QDialog, Ui_fake):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_fake.__init__(self)
        self.setupUi(self)


class Nuevo_proveedor(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.proveedor_button_newProveedor.clicked.connect(self.agregar)

    def agregar(self):
        string_texto = str(self.proveedor_text_newProveedor.toPlainText())
        string_procesado = ''.join(string_texto.split())
        texto = [string_procesado]
        if string_texto == '':
            self.pop = Pop_up()
            self.pop.show()
        else:
            ejecucion = ingresar_proveedor(texto)
            if ejecucion[0] == 'T':
                self.pop = Pop_up()
                self.pop.show()
        self.proveedor_text_newProveedor.clear()
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Nuevo_proveedor()
    window.show()
    sys.exit(app.exec_())
