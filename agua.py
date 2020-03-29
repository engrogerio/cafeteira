from abc import ABC, abstractmethod

class Estado(ABC):

	@abstractmethod
	def aquecer(self):
		...

	def esfriar(self):
		...

	def __repr__(self):
		return self.__class__.__name__ 

class EstadoSolido(Estado):

	def aquecer(self):
		return EstadoLiquido()

	def esfriar(self):
		return EstadoSolido()


class EstadoLiquido(Estado):

	def aquecer(self):
		return EstadoGasoso()

	def esfriar(self):
		return EstadoSolido()


class EstadoGasoso(Estado):

	def aquecer(self):
		return EstadoGasoso()

	def esfriar(self):
		return EstadoLiquido()


class Agua():
	
	def __init__(self):
		self.state = EstadoLiquido()

	def aquecer(self):
		self.state = self.state.aquecer()
		
	def esfriar(self):
		self.state = self.state.esfriar()
	
	def __repr__(self):
		return f'Agua em {self.state}'



