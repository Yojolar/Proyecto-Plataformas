from PyQt5 import uic, QtWidgets
from Funciones_DB import buscar_productos, buscar_cantidad, buscar_precio
from Funciones_DB import revisar_venta, hacer_venta
# from Menu import Menu
qtCreatorFile = 'ventana.ui'
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


class Venta(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.lista_ventas = []
        self.Cobro = 0
        self.revision = ()

        listaProductos = self.actualizar_lista('prod')
        self.venta_producto_box.addItems(listaProductos)
        self.venta_producto_box.currentIndexChanged.connect(self.cantidad)
        self.venta_button_agregarProducto.clicked.connect(self.revisar_venta)
        self.venta_button_finalizaVenta.clicked.connect(self.agregar_venta)
        self.venta_listWidget_inventario.itemDoubleClicked.connect(self.quitar)
        # self.venta_button_regresar.clicked.connect(self.devolver)

    def actualizar_lista(self, var):
        if var == 'prod':
            lista = buscar_productos()
            self.venta_producto_box.insertItem(0, '')
        return lista

    def cantidad(self):
        self.venta_cantidad_box.clear()
        producto = self.venta_producto_box.currentText()
        if producto == '':
            self.venta_label_unidad_2.setText('0')
        else:
            cuantity = buscar_cantidad(str(producto))
            print('QUIERO VER MMM: ', cuantity)
            #if cuantity is None:
            #    self.venta_producto_box.currentIndex.takeItem()
            #    self.pop = Pop_up()
            #    self.pop.show()
            #else:
            lista = cuantity[1]
            self.venta_cantidad_box.addItems(lista)
            precio_unitario = buscar_precio(producto)
            self.venta_label_unidad_2.setText(str(precio_unitario))

    def revisar_venta(self):

        venta = ['', '', '']
        producto = self.venta_producto_box.currentText()
        a = self.venta_cantidad_box.currentText()

        nombre = self.venta_cliente_text_2.toPlainText()
        if nombre == '' or a == '' or producto == '':
            self.pop = Pop_up()
            self.pop.show()
        else:
            cant_base = buscar_cantidad(str(producto))[0]
            cantidad = int(a)
            actual = cant_base - cantidad

            if actual == 0:
                # esconder el item borrar el item de la lista
                pass
            else:
                self.venta_cantidad_box.clear()
                for i in range(1, actual+1):
                    self.venta_cantidad_box.addItem(str(i))

            self.venta_cliente_text_2.setReadOnly(True)
            #cantidad = int(a)
            precio_unitario = buscar_precio(producto)
            mult = precio_unitario*cantidad
            venta_string = '{}   {}   + {}'.format(a, producto, mult)
            self.venta_listWidget_inventario.addItem(venta_string)
            venta[0] = nombre
            venta[1] = producto
            venta[2] = cantidad
            self.lista_ventas.append(venta)
            self.Cobro = self.Cobro + mult
            self.venta_precio_final.setText(str(self.Cobro))
            self.revision = revisar_venta(self.lista_ventas)
            #self.venta_button_regresar.clicked.connect(self.devolver)

    def agregar_venta(self):
        print('HACIENDO VENTA CON: ')
        print()
        if len(self.revision) == 0:
            self.pop = Pop_up()
            self.pop.show()

        else:
            # Limpiar todo:
            hacer_venta(self.revision[1], self.revision[2], self.revision[3])
            self.lista_ventas = []
            self.Cobro = 0
            self.revision = ()
            self.venta_cliente_text_2.clear()
            self.venta_cliente_text_2.setReadOnly(False)
            self.venta_listWidget_inventario.clear()
            self.venta_producto_box.setCurrentIndex(0)
            self.venta_precio_final.setText('0')
            self.venta_producto_box.clear()
            listaProductos = self.actualizar_lista('prod')
            self.venta_producto_box.addItems(listaProductos)
            self.close()
            # print('VENTA ACABADA: ')
            # print()
            # print('lista_ventas: ', self.lista_ventas)
            # print('Cobro: ', self.Cobro)
            # print('revision: ', self.revision)

    def devolver(self):
        print('estoy aqui')
        self.close()
        self.fake = Inicio_fake()
        self.fake.show()

    def quitar(self):
        index_clicked = self.venta_listWidget_inventario.currentRow()
        print(self.lista_ventas[index_clicked])
        precio_unitario = buscar_precio(self.lista_ventas[index_clicked][1])
        cantidad = self.lista_ventas[index_clicked][2]
        mult = precio_unitario*cantidad
        del self.lista_ventas[index_clicked]
        self.venta_listWidget_inventario.takeItem(index_clicked)


        print()
        print('precio_unitario: ', precio_unitario)
        print('cantidad: ', cantidad)
        self.Cobro = self.Cobro - mult
        print('Cuando quito queda: ', self.Cobro)
        self.venta_precio_final.setText(str(self.Cobro))
        self.revision = revisar_venta(self.lista_ventas)
        print(self.revision)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Venta()
    window.show()
    sys.exit(app.exec_())
