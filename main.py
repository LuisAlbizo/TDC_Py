try:
	error=True
	from conjuntos import *
	from basicos import limpiar, pausa, mostrarTexto
except ImportError:
	error=False
	print "Error\nFaltan archivos para la ejecucion de este programa"

text="texto.txt"

class main:
	def __init__(self,conjunto):
		self.conjunto=conjunto
		limpiar()
		print "Teoria de conjuntos"
		while True:
			print "Menu principal\n"
			print "Opcion 0: Teoria"
			print "Opcion 1: Crear conjuntos"
			print "Opcion 2: Pertenencia"
			print "Opcion 3: Operaciones con conjuntos"
			print "Salir[s/S]"
			print "Mas[m/M]"
			opc=raw_input("\nEscoge tu opcion: ")
			limpiar()
			if opc=="0":
				mostrarTexto(text,2,18)
				pausa()
			elif opc=="m" or opc=="M":
				self.ayuda()
			elif opc=="1":
				self.menuCrear()
			elif opc=="2":
				self.menuPertenencia()
			elif opc=="3":
				self.menuOperaciones()
			elif opc=="s" or opc == "S":
				pausa("Adios\n\nEnter para salir")
				exit()
			else:
				print "Opcion invalida"
	
	def pedir2conjuntos(self):
		nohuboerror=True
		try:
			nom1=raw_input("Primer conjunto: ")
			con1=self.conjunto[nom1]
			print nom1,str(con1)
		except:
			con1="None"
			print "El conjunto",nom1,"no existe"
			nohuboerror=False
		if nohuboerror:
			try:
				nom2=raw_input("Segundo conjunto: ")
				con2=self.conjunto[nom2]
				print nom2,str(con2)
			except:
				con2="None"
				print "El conjunto",nom2,"no existe"
				nohuboerror=False
		else:
			con2="None"
			nom2="None"
		return {"error":nohuboerror,"con1":con1,"con2":con2,"nom1":nom1,"nom2":nom2}
	
	def menuCrear(self):
		cc=crearConjuntos(self.conjunto)
		while True:
			print "Opcion 1: Agregar conjunto"
			print "Opcion 2: Ocserbar conjunto"
			print "Opcion 3: Guardar cambios"
			print "Volver al menu principal[s/S]"
			opc=raw_input("\nEscoge tu opcion: ")
			limpiar()
			if opc=="s" or opc == "S":
				break
			elif opc=="1":
				cc.agregarConjunto()
				pausa("\nPresione enter")
			elif opc=="2":
				cc.mostrarConjunto()
				pausa()
			elif opc=="3":
				try:
					cc.guardarCambios()
					print "Cambios guardados con exito"
				except:
					print "No se pudieron guardar los cambios"
				pausa()
			else:
				print "Opcion invalida"

	def menuPertenencia(self):
		pe=Pertenencia()
		while True:
			print "Menu para verificar pertenencias entre conjuntos\n"
			print "Opcion 0: Teoria"
			print "Opcion 1: Subconjunto"
			print "Opcion 2: Superconjunto"
			print "Opcion 3: Igualdad"
			print "Opcion 4: Subconjunto propio"
			print "Opcion 5: Disjunto o conjunto ajeno"
			print "Opcion 6: Propiedades completas de 2 conjuntos"
			print "Volver al menu principal[s/S]"
			opc=raw_input("\nEscoge tu opcion: ")
			limpiar()
			if opc=="s" or opc == "S":
				break
			elif opc=="0":
				while True:
					mostrarTexto(text,20,31)
					sub=raw_input("Regresar[s/S]\n\nEscoge un subtema: ")
					limpiar()
					if sub=="1":
						mostrarTexto(text,32,39)
						pausa()
					elif sub=="2":
						mostrarTexto(text,40,47)
						pausa()
					elif sub=="3":
						mostrarTexto(text,48,52)
						pausa()
					elif sub=="4":
						mostrarTexto(text,53,59)
						pausa()
					elif sub=="s" or sub=="S":	
						break
					else:
						print "Opcion invalida"
			elif opc=="1":
				c=self.pedir2conjuntos()
				if c["error"]:
					pe.subConjunto(c["con1"],c["con2"],c["nom1"],c["nom2"],"imp")
				pausa()
			elif opc=="2":
				c=self.pedir2conjuntos()
				if c["error"]:
					pe.superConjunto(c["con1"],c["con2"],c["nom1"],c["nom2"],"imp")
				pausa()
			elif opc=="3":
				c=self.pedir2conjuntos()
				if c["error"]:
					pe.iguales(c["con1"],c["con2"],c["nom1"],c["nom2"],"imp")
				pausa()
			elif opc=="4":
				c=self.pedir2conjuntos()
				if c["error"]:
					pe.subConjuntoPropio(c["con1"],c["con2"],c["nom1"],c["nom2"],"imp")
				pausa()
			elif opc=="5":
				c=self.pedir2conjuntos()
				if c["error"]:
					pe.disjunto(c["con1"],c["con2"],c["nom1"],c["nom2"],"imp")
				pausa()
			elif opc=="6":
				c=self.pedir2conjuntos()
				nohuboerror=c["error"]
				con1=c["con1"]
				con2=c["con2"]
				nom1=c["nom1"]
				nom2=c["nom2"]
				if nohuboerror:
					pe.subConjunto(con1,con2,nom1,nom2,"imp")
					pe.subConjunto(con2,con1,nom2,nom1,"imp")
					pe.superConjunto(con1,con2,nom1,nom2,"imp")
					pe.superConjunto(con2,con1,nom2,nom1,"imp")
					pe.iguales(con1,con2,nom1,nom2,"imp")
					pe.subConjuntoPropio(con1,con2,nom1,nom2,"imp")
					pe.subConjuntoPropio(con2,con1,nom2,nom1,"imp")
					pe.disjunto(con1,con2,nom1,nom2,"imp")
				pausa()
			else:
				print "Opcion invalida"
	
	def menuOperaciones(self):
		op=Operaciones()
		while True:
			print "Menu para realizar operaciones entre conjuntos\n"
			print "Opcion 0: Teoria"
			print "Opcion 1: Union"
			print "Opcion 2: Interseccion"
			print "Opcion 3: Diferencia"
			print "Opcion 4: Diferencia simetrica"
			print "Opcion 5: Complemento"
			print "Volver al menu principal[s/S]\n"
			opc=raw_input("Escoge tu opcion: ")
			limpiar()
			if opc=="s" or opc=="S":
				break
			elif opc=="0":
				while True:
					mostrarTexto(text,61,69)
					sub=raw_input("Regresar[s/S]\n\nEscoge un subtema: ")
					limpiar()
					if sub=="1" or sub == "u":
						mostrarTexto(text,70,76)
						pausa()
					elif sub=="2" or sub== "n":
						mostrarTexto(text,77,83)
						pausa()
					elif sub=="3" or sub == "\\":
						mostrarTexto(text,84,93)
						pausa()
					elif sub=="4" or sub == "/\\":
						mostrarTexto(text,94,104)
						pausa()
					elif sub =="5" or sub == "'":
						mostrarTexto(text,105,116)
						pausa()
					elif sub == "o" or sub == "O":
						mostrarTexto(text,117,127)
						pausa()
					elif sub=="s" or sub=="S":	
						break
					else:
						print "Opcion invalida"
			elif opc=="1":
				print "Union"
				c=self.pedir2conjuntos()
				if c["error"]:
					op.union(c["con1"],c["con2"],c["nom1"],c["nom2"],"imp")
				pausa()
			elif opc=="2":
				print "Interseccion"
				c=self.pedir2conjuntos()
				if c["error"]:
					op.interseccion(c["con1"],c["con2"],c["nom1"],c["nom2"],"imp")
				pausa()
			elif opc=="3":
				print "Diferencia"
				c=self.pedir2conjuntos()
				if c["error"]:
					op.diferencia(c["con1"],c["con2"],c["nom1"],c["nom2"],"imp")
				pausa()
			elif opc=="4":
				print "Diferencia simetrica"
				c=self.pedir2conjuntos()
				if c["error"]:
					op.diferenciaSimetrica(c["con1"],c["con2"],c["nom1"],c["nom2"],"imp")
				pausa()
			elif opc=="5":
				print "Complemento"
				c=self.pedir2conjuntos()
				if c["error"]:
					op.complemento(c["con1"],c["con2"],c["nom1"],c["nom2"],"imp")
				pausa()
			else:
				print "Opcion invalida"
	
	def ayuda(self):
		print "Este programa sirve para crear simulaciones de conjuntos\nmas bien son listas de numeros o cadenas (se puede crear un conjunto con ambos tipos de datos)"
		print "Y se puede verificar pertenencia entre 2 conjuntos que el usuario defina (aunque probablemente yo sea el unico usuario :'v)"
		print "Este programa solo es una practica de la teoria de conjuntos, hecho por Luis Albizo el 24/06-01/07/2016"
		pausa()

if error:
	try:
		menu=main(conjunto)
	except:
		pausa("Ocurrio un error desconocido\n")
		exit()

#Luis Albizo 27/06/16
