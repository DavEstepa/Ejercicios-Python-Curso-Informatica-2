import sys
import pyqtgraph as pg
from PyQt5 import QtWidgets, uic
import matplotlib.image as mpimg
import numpy as np
from scipy import ndimage
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')

class Filtros(QtWidgets.QDialog):
    def __init__(self, ventanaPrincipal):
        super(Filtros, self).__init__()
        uic.loadUi('DialFiltro.ui', self)
        self.__ventanaPrincipal = ventanaPrincipal
        
        self.filtro1.clicked.connect(self.__appFilt1)
        self.filtro2.clicked.connect(self.__appFilt2)
        self.filtro3.clicked.connect(self.__appFilt3)
        self.original.clicked.connect(self.__appOrig)
    def __appFilt1(self):
        self.__ventanaPrincipal._appFilt1()
        
    def __appFilt2(self):
        self.__ventanaPrincipal._appFilt2()
        
    def __appFilt3(self):
        self.__ventanaPrincipal._appFilt3()
    def __appOrig(self):
        self.__ventanaPrincipal._appOrig()
        
class Ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ventana, self).__init__()
        uic.loadUi('PrincipalFiltros.ui', self)
        self.__ruta= ''
        self.__imgCargada = False
        
        self.asigImagen.clicked.connect(self._graficar)
        self.asigFiltros.clicked.connect(self.__abrirFiltros)
        
    def _appFilt1(self):
        self.graficador.setImage(ndimage.gaussian_filter(self.__img, sigma=(10,10,0)), axes= {'x':1, 'y':0, 'c':2})
        
    def _appFilt2(self):
        self.graficador.setImage(ndimage.uniform_filter(self.__img, size=(10,10,0)), axes= {'x':1, 'y':0, 'c':2})
        
    def _appFilt3(self):
        self.graficador.setImage(ndimage.maximum_filter(self.__img, size=(10,10,0)), axes= {'x':1, 'y':0, 'c':2})
    
    def _appOrig(self):
        self.graficador.setImage(self.__img, axes= {'x':1, 'y':0, 'c':2})
        
    def __abrirFiltros(self):
        self.ventFiltros = Filtros(self)
        self.ventFiltros.show()
        
    def __cargarImagen(self):
        self.__ruta, _ = QtWidgets.QFileDialog.getOpenFileName(
                self,
                "Seleccione un directorio");
        if self.__ruta != '':
            try:
                self.__img=mpimg.imread(self.__ruta)
                self.__imgCargada = True
                
            except:
                self.__imgCargada = False
                alerta=QtWidgets.QMessageBox()
                alerta.setText('Seleccione una Imagen')
                alerta.setWindowTitle('Advertencia')
                alerta.exec_()
        else:
            self.__imgCargada = False
        
    def _graficar(self):
        print('asdfasdfasdf')
        self.__cargarImagen()
        if self.__imgCargada:
            self.asigFiltros.setEnabled(self.__imgCargada)
            self.graficador.setImage(self.__img, axes= {'x':1, 'y':0, 'c':2})
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Ventana()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()