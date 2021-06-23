import unittest

from Calculo import Calculo

class TesteCalculo( unittest.TestCase ):

	def teste_somar(self):
		self.assertEqual( Calculo.somar(2,3) , 5 )

	def teste_subtrair(self):
		c = Calculo()
		self.assertEqual( c.subtrair(5, 3) ,  2 )

	def teste_somarErrado(self):
		self.assertEqual( Calculo.somar(2,3) , 4 )

	def teste_subtrairErrado(self):
		c = Calculo()
		self.assertEqual( c.subtrair(5, 3) ,  3 )