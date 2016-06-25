from conjunto import conjunto
from c import *

def rc():
	print "\n"

class Conjuntos:
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

def guardarConjunto():
	conj=conjunto
	f=open("conjunto.py","w")
	f.write("conjunto="+str(conj))

#LuisAlbizo 24/06/16
