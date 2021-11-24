from examenGeneral import examenGeneral as examenGeneral

class recuentoSanguineoCompleto(examenGeneral):
    def __init__(self):
        self.__cantGlobRojos = None
        self.__cantGlobBlancos = None
        self.__cantPlaquetas = None
        self.__cantHemoglobina = None
    
    def verGlobRojos(self):
        return self.__cantGlobRojos
    
    def verGlobBlancos(self):
        return self.__cantGlobBlancos
    
    def verPlaquetas(self):
        return self.__cantPlaquetas
    
    def verHemoglobina(self):
        return self.__cantHemoglobina
    
    def asignarGlobRojos(self, cantGlobRojos):
        self.__cantGlobRojos = cantGlobRojos
        return True
    
    def asignarGlobBlancos(self, cantGlobBlancos):
        self.__cantGlobBlancos = cantGlobBlancos
        return True
    
    def asignarPlaquetas(self, cantPlaquetas):
        self.__cantPlaquetas = cantPlaquetas
        return True
    
    def asignarHemoglobina(self, cantHemoglobina):
        self.__cantHemoglobina = cantHemoglobina
        return True
    
    def __str__(self):
        return f"""
    EXAMEN DE RECUENTO SANQUINEO---
    Id del examen: {self.verId()}
    Fecha: {self.verFecha()}
    Metodo: {self.verMetodoToma()}
    Medico solicitante: {self.verMedico()}
    
    Resultados:
    Globulos Rojos: {self.verGlobRojos()} --- Globulos Blancos: {self.verGlobBlancos()}
    Plaquetas: {self.verPlaquetas()} --- Hemoglobina: {self.verHemoglobina()}
    * --- *
    """

class panelTiroideoCompleto(examenGeneral):
    def __init__(self):
        self.__cantTSH = None
        self.__cantT4total = None
        self.__cantT4libre = None
        self.__cantT3total = None
        self.__cantT3libre = None
        
    def verTSH(self):
        return self.__cantTSH
    
    def verT4total(self):
        return self.__cantT4total
    
    def verT4libre(self):
        return self.__cantT4libre
    
    def verT3total(self):
        return self.__cantT3total
    
    def verT3libre(self):
        return self.__cantT3libre
    
    def asignarTSH(self, TSH):
        self.__cantTSH = TSH
        return True
    
    def asignarT4total(self, T4total):
        self.__cantT4total = T4total
        return True
    
    def asignarT4libre(self, T4libre):
        self.__cantT4libre = T4libre
        return True
    
    def asignarT3total(self, T3total):
        self.__cantT3total = T3total
        return True
    
    def asignarT3libre(self, T3libre):
        self.__cantT3libre = T3libre
        return True
    
    def __str__(self):
        return f"""
    EXAMEN DE PANEL TIROIDEO COMPLETO---
    Id del examen: {self.verId()}
    Fecha: {self.verFecha()}
    Metodo: {self.verMetodoToma()}
    Medico solicitante: {self.verMedico()}
    
    Resultados:
    TSH: {self.verTSH()} --- T4 Total: {self.verT4total()}
    T4 Libre: {self.verT4libre()} --- T3 Total: {self.verT3total()}
    T3 Libre: {self.verT3libre()}
    * --- *
    """

class perfilBioquímicoCompleto(examenGeneral):
    def __init__(self):
        self.__cantGlucosa = None
        self.__cantBilirrubina = None
        self.__cantCreatinina = None
        
    def verGlucosa(self):
        return self.__cantGlucosa
    
    def verBilirrubina(self):
        return self.__cantBilirrubina
    
    def verCreatinina(self):
        return self.__cantCreatinina
    
    def asignarGlucosa(self, Glucosa):
        self.__cantGlucosa = Glucosa
        return True
    
    def asignarBilirrubina(self, Bilirrubina):
        self.__cantBilirrubina = Bilirrubina
        return True
    
    def asignarCreatinina(self, Creatinina):
        self.__cantCreatinina = Creatinina
        return True
    
    def __str__(self):
        return f"""
    EXAMEN DE PERFIL BIOQUIMICO COMPLETO---
    Id del examen: {self.verId()}
    Fecha: {self.verFecha()}
    Metodo: {self.verMetodoToma()}
    Medico solicitante: {self.verMedico()}
    
    Resultados:
    Glucosa: {self.verGlucosa()} --- Bilirrubina: {self.verBilirrubina()}
    Creatinina: {self.verCreatinina()} --- 
    * --- *
    """
    
class perfilLipidico(examenGeneral):
    def __init__(self):
        self.__cantColesterolTotal = None
        self.__cantHDL = None
        self.__cantVLDL = None
        self.__cantTrigliceridos = None
        
    def verColesterolTotal(self):
        return self.__cantColesterolTotal
    
    def verHDL(self):
        return self.__cantHDL
    
    def verVLDL(self):
        return self.__cantVLDL
    
    def verTrigliceridos(self):
        return self.__cantTrigliceridos
    
    def asignarColesterolTotal(self, ColesterolTotal):
        self.__cantColesterolTotal = ColesterolTotal
        return True
    
    def asignarHDL(self, HDL):
        self.__cantHDL = HDL
        return True
    
    def asignarVLDL(self, VLDL):
        self.__cantVLDL = VLDL
        return True
    
    def asignarTrigliceridos(self, Trigliceridos):
        self.__cantTrigliceridos = Trigliceridos
        return True
    
    def __str__(self):
        return f"""
    EXAMEN DE PERFIL LIPIDICO---
    Id del examen: {self.verId()}
    Fecha: {self.verFecha()}
    Metodo: {self.verMetodoToma()}
    Medico solicitante: {self.verMedico()}
    
    Resultados:
    HDL: {self.verHDL()} --- Colesterol Total: {self.verColesterolTotal()()}
    VLDL: {self.verVLDL()} --- Trigliceridos: {self.verTrigliceridos()()}
    * --- *
    """
    
class acidoUrico(examenGeneral):
    def __init__(self):
        self.__cantAcidoUrico = None
        
    def verAcidoUrico(self):
        return self.__cantAcidoUrico
    
    def asignarAcidoUrico(self, AcidoUrico):
        self.__cantAcidoUrico = AcidoUrico
        return True
    
    def __str__(self):
        return f"""
    EXAMEN DE PANEL TIROIDEO COMPLETO---
    Id del examen: {self.verId()}
    Fecha: {self.verFecha()}
    Metodo: {self.verMetodoToma()}
    Medico solicitante: {self.verMedico()}
    
    Resultados:
    Acido Urico: {self.verAcidoUrico()} --- 
    * --- *
    """