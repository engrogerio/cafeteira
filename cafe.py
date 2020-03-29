import sys

from abc import ABC, abstractmethod

class Estado(ABC):


	@abstractmethod
	def ligar(self):
		pass

	@abstractmethod
	def desligar(self):
		pass

	@abstractmethod
	def colocar_agua(self):
		pass
	
	@abstractmethod
	def colocar_cafe(self):
		pass

	@abstractmethod
	def colocar_bule(self):
		pass	  
	
	@abstractmethod
	def tirar_bule(self):
		pass	  

	@abstractmethod
	def passar_cafe(self):
		pass

class Ligado(Estado):


	def __repr__(self):
		return str(self.__class__.__name__)
	
	def ligar(self):
		return Ligado()

	def desligar(self):
		return Desligado()

	def colocar_agua(self):
		return AguaAbastecida()
	
	def colocar_cafe(self):
		return CafeAbastecido()

	def colocar_bule(self):
		return self
	
	def tirar_bule(self):
		return self 	  

	def passar_cafe(self):
		return self

class Desligado(Estado):

	
	def __repr__(self):
		return self.__class__.__name__	
	
	def ligar(self):
		return Ligado()

	def desligar(self):
		return self

	def colocar_agua(self):
		return self
	
	def colocar_cafe(self):
		return self

	def colocar_bule(self):
		return self
	
	def tirar_bule(self):
		return self

	def passar_cafe(self):
		return self

class AguaAbastecida(Estado):


	def __repr__(self):
		return str(self.__class__.__name__)

	def ligar(self):
		return self

	def desligar(self):
		return Desligado()

	def colocar_agua(self):
		return self
	
	def colocar_cafe(self):
		return CafeAbastecido()

	def colocar_bule(self):
		return self
	
	def tirar_bule(self):
		return self

	def passar_cafe(self):
		return self

class CafeAbastecido(Estado):


	def __repr__(self):
		return str(self.__class__.__name__)

	def ligar(self):
		return self

	def desligar(self):
		return Desligado()

	def colocar_agua(self):
		return AguaAbastecida()
	
	def colocar_cafe(self):
		return self

	def colocar_bule(self):
		return BuleColocado()
	
	def tirar_bule(self):
		return self

	def passar_cafe(self):
		return self

class CafeteiraAbastecida(Estado):
	

	def __repr__(self):
		return str(self.__class__.__name__)

	def ligar(self):
		return self

	def desligar(self):
		return Desligado()

	def colocar_agua(self):
		return self
	
	def colocar_cafe(self):
		return self

	def colocar_bule(self):
		return BuleColocado()
	
	def tirar_bule(self):
		return self

	def passar_cafe(self):
		return self

class BuleColocado(Estado):


	def __repr__(self):
		return str(self.__class__.__name__)

	def ligar(self):
		return self

	def desligar(self):
		return Desligado()

	def colocar_agua(self):
		return self
	
	def colocar_cafe(self):
		return self

	def colocar_bule(self):
		return self
	
	def tirar_bule(self):
		return AguardandoBuleParaPassar()	  

	def passar_cafe(self):
		return Aquecendo()

class Aquecendo(Estado):


	def __repr__(self):
		return str(self.__class__.__name__)

	def ligar(self):
		return self

	def desligar(self):
		return Desligado()

	def colocar_agua(self):
		return self
	
	def colocar_cafe(self):
		return self

	def colocar_bule(self):
		return self
	
	def tirar_bule(self):
		return AguardandoBuleParaPassar()	  

	def passar_cafe(self):
		return self

class AguardandoBuleParaPassar(Estado):


	def __repr__(self):
		return str(self.__class__.__name__)

	def ligar(self):
		return self

	def desligar(self):
		return Desligado()

	def colocar_agua(self):
		return self
	
	def colocar_cafe(self):
		return self

	def colocar_bule(self):
		return BuleColocado()	  
	
	def tirar_bule(self):
		return self

	def passar_cafe(self):
		return self

class AguardandoBuleParaAquecer(Estado):


	def __repr__(self):
		return str(self.__class__.__name__)

	def ligar(self):
		return self

	def desligar(self):
		return Desligado()

	def colocar_agua(self):
		return self
	
	def colocar_cafe(self):
		return self

	def colocar_bule(self):
		return Aquecendo()	  
	
	def tirar_bule(self):
		return self

	def passar_cafe(self):
		return self


class Aquecendo(Estado):


	def __repr__(self):
		return str(self.__class__.__name__)

	def ligar(self):
		return self

	def desligar(self):
		return Desligado()

	def colocar_agua(self):
		return self
	
	def colocar_cafe(self):
		return self

	def colocar_bule(self):
		return self
	
	def tirar_bule(self):
		return AguardandoBuleParaAquecer()	  

	def passar_cafe(self):
		return self

class Cafeteira:


	def __init__(self):
		self.state = Desligado()
				
	def ligar(self):
		self.state = self.state.ligar()
		return self.state

	def desligar(self):
		self.state = self.state.desligar()
		return self.state

	def colocar_agua(self):
		self.state = self.state.colocar_agua()
		return self.state
	
	def colocar_cafe(self):
		self.state = self.state.colocar_cafe()
		return self.state

	def colocar_bule(self):
		self.state = self.state.colocar_bule()
		return self.state
	
	def tirar_bule(self):
		self.state = self.state.tirar_bule()	  
		return self.state

	def passar_cafe(self):
		self.state = self.state.passar_cafe()
		return self.state


def get_methods(instance):
	methods_list = dir(instance)
	dic = {}
	methods = [m for m in methods_list if not m.startswith('_') and m !='state']
	for n, method in enumerate(methods):
		result = getattr(instance, method)
		dic[str(n+1)] = {"function": result, "name": method.replace('_',' ')}
		dic['q'] = {"function": exit, "name": "sair"}
	return dic

if __name__ == "__main__":
	cafeteira = Cafeteira()
	print('\n')
	print('Estado = Desligado')
	print('\n')
	while True:
		methods = get_methods(cafeteira)
		for key, method in methods.items():
			method_name = method['name']
			print(f'{key} = {method_name}')
		valid_entries = [str(n) for n in methods.keys()]
		action = 0
		while action not in valid_entries:
			action = input('\n Escolha a Operação > ')
		call = methods.get(action)['function']
		x = call()
		print('\n')
		print('Estado =', str(x))
		print('\n')
