class ADNseq:
    def __init__(self):
        self.__secuencia = ''
        self.__secComplementaria = ''
        self.__valida = None
        self.__numElementos = {}
        self.__basesValidas = {'A', 'T', 'C', 'G'}
        self.__conversionBases = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        
    def leerSecuencia(self, ruta = ''):
        try:
            with open(ruta) as archivo:
                self.__secuencia = archivo.read()
                self.__valida = None
                self.__numElementos = {}
                self.__secComplementaria = ''
        except:
            print('Ruta incorrecta')
            return None
            
    def esValida(self):
        if self.__secuencia == '':  
            self.__valida = all([base in self.__basesValidas for base in set(self.__secuencia)])
            if self.__valida:
                print('La secuencia es valida')
            else:
                print('La secuencia es invalida')
            return self.__valida
        else:
            print('No hay una secuencia cargada')
            return None
    
    def generarComplementaria(self):
        if self.esValida():
            self.__secComplementaria = ''.join([self.__conversionBases[base] for base in self.__secuencia])
        else: print('La secuencia no representa un segmento de ADN')
        
    def verSecuenciaComplementaria(self):
        return self.__secComplementaria
    
    def verSecuenciaOriginal(self):
        return self.__secuencia
        
    def contarElementos(self):
        _ = [self.__numElementos.update({nuevaLlave: 0}) for nuevaLlave in set(self.__secuencia)]
        for llave in self.__secuencia:
            self.__numElementos[llave] += 1
        return self.__numElementos
    
    
miSecuencia = ADNseq()
miSecuencia.leerSecuencia('secuencia1.txt')
miSecuencia.contarElementos()