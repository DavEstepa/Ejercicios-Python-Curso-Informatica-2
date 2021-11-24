import examenes as tipo

class sistema:
    def __init__(self):
        self.__baseDeDatos = {}
        self.__objetivo = None
        self.__estadoMenu = 0
        self.__estado = 0
        self.__examen = None
        
        self.__msj1 = """
        BIENVENIDO AL CENTRO DE GESTION DE EXAMENES DE SANGRE
        ingrese el numero en funcion de lo que desee hacer
        
        1. Ingresar examen
        2. Ver examen / historial de paciente
        3. Salir
        """
        
        self.__msj2 = """
        BIENVENIDO AL CENTRO DE GESTION DE EXAMENES DE SANGRE
        ingrese el numero en funcion de lo que desee hacer
        
        --> Ingresar Examen
        1. Recuento de sangre completo
        2. Panel Tiroideo completo
        3. Perfil bioquimico completo
        4. Perfil lipidico
        5. Acido Urico
        6. Regresar al menu principal
        """
        
        self.__msj3 = """
        BIENVENIDO AL CENTRO DE GESTION DE EXAMENES DE SANGRE
        ingrese el numero en funcion de lo que desee hacer
        
        --> Ver examen / historial de paciente
        1. Ver examen
        2. Historial de paciente
        3. Salir
        """
    
    def __examenGeneral(self):
        """Metodo que maneja el ingreso de los valores generales que definen a un examen"""
        self.__examen.asignarId(input('Ingrese el Id del examen: '))
        self.__examen.asignarMedico(input('Ingrese el nombre del medico: '))
        self.__examen.asignarMetodoToma(input('Ingrese el metodo de toma del examen: '))
        self.__examen.asignarFecha(input('Ingrese la fecha de realizacion: '))
    
    def __examenTipo1(self):
        self.__examen = tipo.recuentoSanguineoCompleto()
        self.__examenGeneral()
        self.__examen.asignarGlobRojos(input('Ingrese el valor de Globulos rojos: '))
        self.__examen.asignarGlobBlancos(input('Ingrese el valor de Globulos blancos: '))
        self.__examen.asignarHemoglobina(input('Ingrese el valor de Hemoglobina: '))
        self.__examen.asignarPlaquetas(input('Ingrese el valor de Plaquetas: '))
    
    def __examenTipo2(self):
        self.__examen = tipo.panelTiroideoCompleto()
        self.__examenGeneral()
        self.__examen.asignarTSH(input('Ingrese el valor de TSH: '))
        self.__examen.asignarT4total(input('Ingrese el valor de T4 total: '))
        self.__examen.asignarT4libre(input('Ingrese el valor de T4 libre: '))
        self.__examen.asignarT3total(input('Ingrese el valor de T3 total: '))
        self.__examen.asignarT3libre(input('Ingrese el valor de T3 libre: '))
        
    def __examenTipo3(self):
        self.__examen = tipo.perfilBioquímicoCompleto()
        self.__examenGeneral()
        self.__examen.asignarGlucosa(input('Ingrese el valor de Glucosa: '))
        self.__examen.asignarBilirrubina(input('Ingrese el valor de Bilirrubina: '))
        self.__examen.asignarCreatinina(input('Ingrese el valor de Creatinina: '))
    
    def __examenTipo4(self):
        self.__examen = tipo.perfilLipidico()
        self.__examenGeneral()
        self.__examen.asignarColesterolTotal(input('Ingrese el valor de Colesterol total: '))
        self.__examen.asignarHDL(input('Ingrese el valor de HDL: '))
        self.__examen.asignarVLDL(input('Ingrese el valor de VLDL: '))
        self.__examen.asignarTrigliceridos(input('Ingrese el valor de Trigliceridos: '))
    
    def __examenTipo5(self):
        self.__examen = tipo.acidoUrico()
        self.__examenGeneral()
        self.__examen.asignarAcidoUrico(input('Ingrese el valor de Acido Urico: '))
    
    def __buscarExamen_Id(self, clave):
        for paciente in self.__baseDeDatos.keys():
            for exm in self.__baseDeDatos[paciente]:
                if clave == exm.verId():
                    self.__examen = exm
                    return True
        return False
    
    def __ingresarExamen(self):
        if self.__estadoMenu == 0:
            print(self.__msj2)
            self.__estadoMenu = int(input('Opcion ingresada: '))
            if self.__estadoMenu == 6:
                self.__estado = 0
                
            else:
                self.__objetivo = input('Ingrese el nombre del paciente: ')
                if self.__objetivo in self.__baseDeDatos.keys():
                    pass
                else:
                    self.__baseDeDatos[self.__objetivo] = []
                
        elif self.__estadoMenu == 1:   
            self.__examenTipo1()
        elif self.__estadoMenu == 2:
            self.__examenTipo2()
        elif self.__estadoMenu == 3:
            self.__examenTipo3()
        elif self.__estadoMenu == 4:
            self.__examenTipo4()
        elif self.__estadoMenu == 5:
            self.__examenTipo5()

            
    def __verExamen(self):
        if self.__estadoMenu == 0:
            print(self.__msj3)
            self.__estadoMenu = int(input('Opcion ingresada: '))
            if self.__estadoMenu == 3:
                self.__estado = 0
                
        elif self.__estadoMenu == 1:
            if self.__buscarExamen_Id(input('Ingrese el Id del examen: ')):
                print(self.__examen)
                self.__examen = None
                input('Oprima enter para continuar')
                self.__estadoMenu = 0
            else:
                print('El id ingresado no corresponde a ningun examen')
                self.__estadoMenu = 0
                
        elif self.__estadoMenu == 2:
            self.__objetivo = input('Ingrese el nombre del paciente: ')
            if self.__objetivo in self.__baseDeDatos.keys():
                for exm in self.__baseDeDatos[self.__objetivo]:
                    print(exm)
                    self.__objetivo = None
                    self.__estadoMenu = 0
                input('Oprima enter para continuar')
            else:
                print('El paciente no esta en el sistema')
                self.__estadoMenu = 0
    
    def iniciar(self):
        while True:
            if self.__estado == 0:
                self.__estadoMenu = 0
                print(self.__msj1)
                self.__estado = int(input('Opcion ingresada: '))
                
            elif self.__estado == 1:
                self.__ingresarExamen()
                if self.__examen != None:
                    self.__estadoMenu = 0
                    self.__baseDeDatos[self.__objetivo].append(self.__examen)
                    self.__examen = None
                    print('...EXAMEN INGRESADO')
                    input('Oprima enter para continuar')
                    
            elif self.__estado == 2:
                self.__verExamen()
                
            elif self.__estado == 3:
                break
            
Sist = sistema().iniciar()