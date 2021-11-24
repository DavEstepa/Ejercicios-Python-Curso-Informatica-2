class historiaClinica:
    def __init__(self):
        self.__nombre = ''
        self.__tipoDocumento = ''
        self.__numeroIdentificacion = None
        self.__idHistoria = None
        self.__grupoSanguineo = None
        
    def verNombre(self):
        return self.__nombre
    
    def verTipoDocumento(self):
        return self.__tipoDocumento
    
    def verNumeroIdentificacion(self):
        return self.__numeroIdentificacion
    
    def veridHistoria(self):
        return self.__idHistoria
    
    def verGrupoSanguineo(self):
        return self.__grupoSanguineo
    
    def asignarNombre(self, nombre):
        self.__nombre = nombre
        return True
    
    def asignarTipoDocumento(self, tipoDocumento):
        self.__tipoDocumento = tipoDocumento
        return True
    
    def asignarNumeroIdentificacion(self, numeroId):
        self.__numeroIdentificacion = numeroId
        return True
    
    def asignarIdHistoria(self, idHistoria):
        self.__idHistoria = idHistoria
        return True
    
    def asignarGrupoSanguineo(self, rh):
        self.__grupoSanguineo = rh
        return True
    
    def __str__(self):
        return f"""
    HISTORIA CLINICA # {self.__idHistoria}
    Paciente: {self.__nombre}
    Identificacion: {self.__tipoDocumento}. {self.__numeroIdentificacion}
    Grupo sanguineo: {self.__grupoSanguineo}
    
    ---
    """