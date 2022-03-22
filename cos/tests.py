from django.test import TestCase
from cos.models import Marca

def is_maior(x):
	if len(x) > 1:
		return True
	else:
		return False

class MarcaTestCase(TestCase):
	def setUp(self):
		Marca.objects.create(nome="Apple", id=1)
		Marca.objects.create(nome="Apple", id=2)

	def testar_marca_duplicada(self):
		"""Verifica se uma marca foi cadastrada mais de uma vez."""
		marcas = Marca.objects.filter(nome="Apple")
		self.assertTrue(is_maior(marcas))

