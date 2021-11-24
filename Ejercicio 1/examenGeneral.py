class examenGeneral:
	def __init__(self):
		self.__fecha = ''
		self.__medico= ''
		self.__metodoToma = ''
		self.__id=None

	def verFecha(self):
		return self.__fecha

	def verMedico(self):
		return self.__medico

	def verMetodoToma(self):
		return self.__metodoToma

	def verId(self):
		return self.__id

	def asignarFecha(self, fecha):
		self.__fecha = fecha
		return True

	def asignarMedico(self, medico):
		self.__medico = medico
		return True

	def asignarMetodoToma(self, metodo):
		self.__metodoToma = metodo
		return True
		
	def asignarId(self, id):
		self.__id = id
		return True