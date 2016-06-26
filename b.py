from conjunto import conjunto
from c import *
from os import system
from time import sleep

def rc():
	print "\n"

class crearConjuntos:
	def __init__(self,conjunto):
		self.a=conjunto
	
	def agregarConjunto(self):
		nombre=raw_input("Escribe el nombre del conjunto a crear:\n")
		elementos=[]
		print "Escribe los elementos:\n['end' para terminar]"
		while True:
			try:
				b=raw_input()
				if b=="end":
					break
				try:
					elementos.append(int(b))
				except:
					elementos.append(b)
			except:
				print "Entrada incorrecta"
		self.a[nombre]=elementos


	def mostrarConjunto(self):
		conjunto=raw_input("Escribe el nombre del conjunto a ocserbar:\n")
		try:
			print self.a[conjunto]
		except:
			print "El conjunto '"+conjunto+"' no existe"

class Pertenencia:
	def subConjunto(self,c1,c2,nombre1="A",nombre2="B",m="ret"):
		if numCoincidencias(c1,c2)==len(c1):
			if m=="ret":
				return True
			elif m=="imp":
				print "El conjunto",nombre1+"es subconjunto del conjunto",nombre2
		else:
			if m=="ret":
				return False
			elif m=="imp":
				print "El conjunto",nombre1,"no es subconjunto del conjunto",nombre2

	def superConjunto(self,c1,c2,nombre1="A",nombre2="B",m="ret"):
		if self.subConjunto(c2,c1):
			if m=="ret":
				return True
			elif m=="imp":
				print "El conjunto",nombre1,"es superconjunto del conjunto",nombre2
		else:
			if m=="ret":
				return False
			elif m=="imp":
				print "El conjunto",nombre1,"no es superconjunto del conjunto",nombre2
	
	def iguales(self,co1,co2,nombre1="A",nombre2="B",m="ret"):
		a=self.subConjunto(co1,co2)
		b=self.subConjunto(co2,co1)
		if a and b:
			if m=="ret":
				return True
			elif m=="imp":
				print "El conjunto",nombre1,"es igual al conjunto",nombre2
		else:
			if m=="ret":
				return False
			elif m=="imp":
				print "El conjunto",nombre1,"no es igual al conjunto",nombre2

	def disjunto(self,c1,c2,nombre1="A",nombre2="B",m="ret"):
		if numCoincidencias(c1,c2)==0:
			if m=="ret":
				return True
			elif m=="imp":
				print "El conjunto",nombre1,"es disjunto de",nombre2
		else:
			if m=="ret":
				return False
			elif m=="imp":
				print "El conjunto",nombre1,"no es disjunto de",nombre2

def guardarConjunto(conjunto):
	conj=conjunto
	f=open("conjunto.py","w")
	f.write("conjunto="+str(conj))

#LuisAlbizo 24/06/16
