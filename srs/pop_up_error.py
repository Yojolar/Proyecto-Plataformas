from PyQt5 import uic, QtWidgets

qtCreatorFile2 = 'venta_pop_Enombre.ui'
Ui_pop, QtBaseClass = uic.loadUiType(qtCreatorFile2)


class Pop_up(QtWidgets.QDialog, Ui_pop):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_pop.__init__(self)
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Pop_up()
    window.show()
    sys.exit(app.exec_())
