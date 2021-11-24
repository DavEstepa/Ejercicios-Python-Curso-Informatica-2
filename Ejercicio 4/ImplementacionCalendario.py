import datetime
import webbrowser as wb
from calendar import HTMLCalendar

class calendario(HTMLCalendar):
    def __init__(self):
        super().__init__()
        self.__mesesCod = {'Enero': 1, 'Febrero': 2, 'Marzo': 3,
                            'Abril': 4, 'Mayo': 5, 'Junio': 6,
                            'Julio': 7, 'Agosto': 8, 'Septiembre': 9,
                            'Octubre': 10, 'Noviembre': 11, 'Diciembre': 12}
        self.__añoActual = datetime.date.today().year
        self.__mesActual = datetime.date.today().month
        self.__contenido = ''
        
    def verMes(self, mes=''):
        if mes == '':
            self.__contenido = self.formatmonth(self.__añoActual, self.__mesActual)
            
        else:
            self.__contenido = self.formatmonth(self.__añoActual, self.__mesesCod[mes])
        
        self.__generarEjecutarHTML()
    
    def verAño(self, año=0):
        if año == 0:
            self.__contenido = self.formatyear(self.__añoActual)
            
        else:
            self.__contenido = self.formatyear(año)
        
        self.__generarEjecutarHTML()
    
    def __generarEjecutarHTML(self):
        with open('index.html', 'w+') as f:
            f.write(self.__contenido)
        wb.open('index.html')
        
calen = calendario()
calen.verAño(1998)
        