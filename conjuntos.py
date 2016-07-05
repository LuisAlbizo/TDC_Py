from fc import conjunto
from herramientas import quitar,numCoincidencias,estaEn,elementosComunes, duplicarLista, eliminarDuplicados, juntarListas
from time import sleep


class crearConjuntos:
	def __init__(self,conjunto,arc="fc.py"):
		self.conjunto=conjunto
		self.arc=arc

	def agregarConjunto(self):
		nombre=raw_input("Escribe el nombre del conjunto a crear:\n")
		elementos=[]
		print "Escribe los elementos:\n['end' para ternminar]"
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

class Operaciones:
	def union(self,c1,c2,n1="A",n2="B",m="ret"):
		if m=="ret":
			return juntarListas(c1,c2)
		elif m=="imp":
			print n1,"u",n2,"=",str(juntarListas(c1,c2))

	def interseccion(self,c1,c2,n1="A",n2="B",m="ret"):
		if m=="ret":
			return elementosComunes(c1,c2)
		elif m=="imp":
			print n1,"n",n2,"=",str(elementosComunes(c1,c2))

	def diferencia(self,c1,c2,n1="A",n2="B",m="ret"):
		if m=="ret":
			return quitar(c1,c2)
		elif m=="imp":
			print n1,"\\",n2,"=",str(quitar(c1,c2))

	def diferenciaSimetrica(self,c1,c2,n1="A",n2="B",m="ret"):
		ds=self.diferencia(c1,c2)+self.diferencia(c2,c1)
		if m=="ret":
			return ds
		elif m=="imp":
			print n1,"/\\",n2,"=",str(ds)
		
	def complemento(self,c1,c2,n1="A",n2="B",m="ret"):
		if m=="ret":
			return quitar(c2,c1)
		elif m=="imp":
			print "Si el conjunto universo es",n1,"u",n2,"osea",str(self.union(c1,c2)),"; entonces el complemento para",n1,"seria:\n"
			print n1+"'","=",str(quitar(c2,c1))


#LuisAlbizo 24/06/16
