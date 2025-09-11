# Empanadas ordering system based on UML diagram
from enum import Enum
from typing import List, Optional

class Sabor(Enum):
	CARNE = 1
	POLLO = 2
	JAMON_Y_QUESO = 3
	VERDURA = 4
	HUMITA = 5

class Item:
	def __init__(self, sabor: Sabor, cant: int):
		self.sabor = sabor
		self.cant = cant

	def getSabor(self) -> Sabor:
		return self.sabor

	def getCant(self) -> int:
		return self.cant

	def setCant(self, cant: int) -> None:
		self.cant = cant

class Pedido:
	def __init__(self, telefono: str, direccion: str, numPedido: int):
		self.telefono = telefono
		self.direccion = direccion
		self.numPedido = numPedido
		self.items: List[Item] = []

	def getTelefono(self) -> str:
		return self.telefono

	def getDireccion(self) -> str:
		return self.direccion

	def getNumero(self) -> int:
		return self.numPedido

	def getItems(self) -> List[Item]:
		return self.items

	def agregarItem(self, item: Item) -> None:
		self.items.append(item)

	def buscarItem(self, sabor: Sabor) -> Optional[Item]:
		for item in self.items:
			if item.getSabor() == sabor:
				return item
		return None

class YaEmpanadas:
	def __init__(self):
		self.pedidos: List[Pedido] = []
		self.next_num = 1

	def crearORecuperarPedido(self, telefono: str, direccion: str) -> int:
		for pedido in self.pedidos:
			if pedido.getTelefono() == telefono and pedido.getDireccion() == direccion:
				return pedido.getNumero()
		nuevo = Pedido(telefono, direccion, self.next_num)
		self.pedidos.append(nuevo)
		self.next_num += 1
		return nuevo.getNumero()

	def cargarEmpanadas(self, numPedido: int, sabor: Sabor, cant: int) -> None:
		pedido = self.buscarPedidoM(numPedido)
		if pedido:
			item = pedido.buscarItem(sabor)
			if item:
				item.setCant(item.getCant() + cant)
			else:
				pedido.agregarItem(Item(sabor, cant))

	def listarPedidoCompleto(self, numPedido: int) -> str:
		pedido = self.buscarPedidoM(numPedido)
		if not pedido:
			return "Pedido no encontrado"
		res = f"Pedido #{pedido.getNumero()} - Tel: {pedido.getTelefono()} - Dir: {pedido.getDireccion()}\n"
		for item in pedido.getItems():
			res += f"  {item.getSabor().name}: {item.getCant()}\n"
		return res.strip()

	def buscarPedidoM(self, numPedido: int) -> Optional[Pedido]:
		for pedido in self.pedidos:
			if pedido.getNumero() == numPedido:
				return pedido
		return None

	def buscarPedidoT(self, telefono: str) -> Optional[Pedido]:
		for pedido in self.pedidos:
			if pedido.getTelefono() == telefono:
				return pedido
		return None
