import sys
import pyqtgraph as pg
from PyQt5 import QtWidgets, uic
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')

class Ventana(QtWidgets.QWidget):
    def __init__(self):
        super(Ventana, self).__init__()
        uic.loadUi('Estructura.ui', self)
        self.__contenido = [0]
        
        self.boton.clicked.connect(self.graficar)

    def graficar(self):
        try:
            self.__contenido.append(int(self.campoIngreso.text()))
            self.pantalla.plot(self.__contenido)
            self.campoIngreso.setText('')
        except:
            alerta=QtWidgets.QMessageBox()
            alerta.setText('Ingrese valores numericos')
            alerta.setWindowTitle('Error')
            alerta.exec_()
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Ventana()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()