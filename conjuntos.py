from fc import conjunto
from herramientas import *
from time import sleep


class crearConjuntos:
	def __init__(self,conjunto,arc="fc.py"):
		self.conjunto=conjunto
		self.arc=arc

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
		self.conjunto[nombre]=elementos

	def mostrarConjunto(self):
		conjunto=raw_input("Escribe el nombre del conjunto a ocserbar:\n")
		try:
			print self.conjunto[conjunto]
		except:
			print "El conjunto '"+conjunto+"' no existe"
	
	def guardarCambios(self):
		cf=open(self.arc,"w")
		cf.write("conjunto="+str(self.conjunto))
		cf.close()

class Pertenencia:
	def subConjunto(self,c1,c2,nombre1="A",nombre2="B",m="ret"):
		if numCoincidencias(c1,c2)==len(c1):
			if m=="ret":
				return True
			elif m=="imp":
				print "El conjunto",nombre1,"es subconjunto del conjunto",nombre2
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
		a=not(self.subConjunto(c1,c2))
		b=not(self.subConjunto(c2,c1))
		c=numCoincidencias(c1,c2)==0
		if len(c1)==0 or len(c2)==0:
			d= a and b
		else:
			d=c
		if d:
			if m=="ret":
				return True
			elif m=="imp":
				print "El conjunto",nombre1,"es disjunto de",nombre2
		else:
			if m=="ret":
				return False
			elif m=="imp":
				print "El conjunto",nombre1,"no es disjunto de",nombre2

	def subConjuntoPropio(self,c1,c2,nombre1="A",nombre2="B",m="ret"):
		if self.subConjunto(c1,c2)==True and self.subConjunto(c2,c1)==False:
			if m=="ret":
				return True
			elif m=="imp":
				print "El conjunto",nombre1,"es subconjunto propio de",nombre2
		else:
			if m=="ret":
				return False
			elif m=="imp":
				print "El conjunto",nombre1,"no es subconjunto propio de",nombre2

"""
def conPo1(con):
	a=[duplicarLista(con)]
	if len(con)==1:
		return []
	else:
		for el in range(0,len(con)):
			c=[]
			for ele in range(0,len(con)):
				if ele!=el:
					c.append(con[ele])
					if len(c)==len(con)-1:
						a.append(c)
	return a

def conPo2(con):
	a=duplicarLista(con)
	i=0
	a=a+conPo1(a)
	for wele in range(0,len(con)):
		a.pop(0)
	for el in range(1,len(con)):
		a=a+conPo1(a[el])[1:]
	return a
---No puedo resolver este problema,
no soy de buscar ayuda en internet de hecho nunca lo he hecho
pero si de aqui a una semana no lo resuelvo de una manera correcta
usando la recursividad bien, buscare algun tutorial en algun foro o algo asi :v
26/06/16---
"""

#LuisAlbizo 24/06/16
