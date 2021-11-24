import historiaClinica as HC
import os

class sistema:
    def __init__(self):
        self.__baseDeDatos = []
        self.__estado = 0
        self.__historiaClinica = None
        self.__totalHC = 0
        self.__cargarHistorias()
        self.__msj1 = """
        GESTION DE HISTORIAS CLINICAS
        ingrese el numero en funcion de lo que desee hacer
        
        1. Ingresar Historia Clinica
        2. Ver Historia Clinica
        3. Salir
        """
    def __almacenarTXT(self):
        with open(f'historiaNum_{self.__totalHC}.txt', 'w+') as f:
            s=f"""{self.__historiaClinica.verNombre()};{self.__historiaClinica.verTipoDocumento()};{self.__historiaClinica.verNumeroIdentificacion()};{self.__historiaClinica.verGrupoSanguineo()}"""
            f.write(s)
    
    def __cargarHistorias(self):
        for archivo in list(filter(None ,[st if '.txt' in st else None for st in os.listdir()])):
            with open(archivo) as f:
                elementosBasicos = f.read().split(';')
                self.__historiaClinica = HC.historiaClinica()
                self.__historiaClinica.asignarNombre(elementosBasicos[0])
                self.__historiaClinica.asignarTipoDocumento(elementosBasicos[1])
                self.__historiaClinica.asignarNumeroIdentificacion(elementosBasicos[2])
                self.__historiaClinica.asignarIdHistoria(str(self.__totalHC))
                self.__historiaClinica.asignarGrupoSanguineo(elementosBasicos[3])
                self.__baseDeDatos.append(self.__historiaClinica)
                self.__totalHC += 1
    
    def __generarHC(self):
        self.__historiaClinica = HC.historiaClinica()
        self.__historiaClinica.asignarNombre(input('Ingrese el Nombre completo: '))
        self.__historiaClinica.asignarTipoDocumento(input('Ingrese el tipo de identificacion: '))
        self.__historiaClinica.asignarNumeroIdentificacion(input('Ingrese el numero de identificacion: '))
        self.__historiaClinica.asignarIdHistoria(str(self.__totalHC))
        self.__historiaClinica.asignarGrupoSanguineo(input('Ingrese el grupo sanguineo: '))
    
    def __buscarHC_Id(self, clave):
        for hc in self.__baseDeDatos:
            if clave == hc.veridHistoria():
                self.__historiaClinica = hc
                return True
        return False
    
    def __ingresarHC(self):
        self.__estado = 0
        self.__generarHC()
        self.__baseDeDatos.append(self.__historiaClinica)
        self.__totalHC += 1
        self.__almacenarTXT()
        self.__historiaClinica = None
        print('...HISTORIA CLINICA INGRESADA')
        input('Oprima enter para continuar')

            
    def __verHC(self):                
        if self.__buscarHC_Id(input('Ingrese el Id de la historia clinica: ')):
            print(self.__historiaClinica)
            self.__historiaClinica = None
            input('Oprima enter para continuar')
            self.__estado = 0
        else:
            print('El id ingresado no corresponde a ningun examen')
            input('Oprima enter para continuar')
            self.__estado = 0
                    
    def iniciar(self):
        while True:
            if self.__estado == 0:
                print(self.__msj1)
                self.__estado = int(input('Opcion ingresada: '))
                
            elif self.__estado == 1:
                self.__ingresarHC()
                    
            elif self.__estado == 2:
                self.__verHC()
                
            elif self.__estado == 3:
                break
            
Sist = sistema().iniciar()