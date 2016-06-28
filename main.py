from conjuntos import *

class main:

	def __init__(self,conjunto):
		self.conjunto=conjunto
		print "Teoria de conjuntos"
		while True:
			print "Menu principal\n"
			print "Opcion 0: Teoria"
			print "Opcion 1: Crear conjuntos"
			print "Opcion 2: Pertenencia"
			print "Opcion 3: Salir"
			print "Mas[m/M]"
			opc=raw_input("\nEscoge tu opcion: ")
			limpiar()
			if opc=="0":
				print "Aun no disponible"
				pausa()
			elif opc=="m" or opc=="M":
				self.ayuda()
			elif opc=="1":
				self.menuCrear()
			elif opc=="2":
				self.menuPertenencia()
			elif opc=="3":
				print "Adios vaquero :'v\n"
				exit()
			else:
				print "Opcion invalida"
				pausa()
	
	def menuCrear(self):
		cc=crearConjuntos(self.conjunto)
		while True:
			print "Opcion 1: Agregar conjunto"
			print "Opcion 2: Ocserbar conjunto"
			print "Opcion 3: Guardar cambios"
			print "Opcion 4: Volver al menu principal"
			opc=raw_input("\nEscoge tu opcion: ")
			limpiar()
			if opc=="4":
				pausa("Presione enter para regresar al menu principal")
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
				pausa()

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
			print "Oocion 6: Volver al menu principal"
			opc=raw_input("\nEscoge tu opcion: ")
			limpiar()
			if opc=="6":
				pausa("Presione enter para regresar al menu principal")
				break
			elif opc=="0":
				print "Proximamente :v...."
				pausa()
			elif opc=="1":
				nom1=raw_input("Primer conjunto: ")
				nom2=raw_input("Segundo conjunto: ")
				nohuboerror=True
				try:
					con1=self.conjunto[nom1]
				except:
					print "El conjunto",nom2,"no existe"
					nohuboerror=False
				try:
					con2=self.conjunto[nom2]
				except:
					print "El conjunto",nom2,"no existe"
					nohuboerror=False
				if nohuboerror:
					pe.subConjunto(con1,con2,nom1,nom2,"imp")
				pausa()
			elif opc=="2":
				nom1=raw_input("Primer conjunto: ")
				nom2=raw_input("Segundo conjunto: ")
				nohuboerror=True
				try:
					con1=self.conjunto[nom1]
				except:
					print "El conjunto",nom1,"no existe"
					nohuboerror=False
				try:
					con2=self.conjunto[nom2]
				except:
					print "El conjunto",nom2,"no existe"
					nohuboerror=False
				if nohuboerror:
					pe.superConjunto(con1,con2,nom1,nom2,"imp")
				pausa()
			elif opc=="3":
				nom1=raw_input("Primer conjunto: ")
				nom2=raw_input("Segundo conjunto: ")
				nohuboerror=True
				try:
					con1=self.conjunto[nom1]
				except:
					print "El conjunto",nom1,"no existe"
					nohuboerror=False
				try:
					con2=self.conjunto[nom2]
				except:
					print "El conjunto",nom2,"no existe"
					nohuboerror=False
				if nohuboerror:
					pe.iguales(con1,con2,nom1,nom2,"imp")
				pausa()
			elif opc=="4":
				nom1=raw_input("Primer conjunto: ")
				nom2=raw_input("Segundo conjunto: ")
				nohuboerror=True
				try:
					con1=self.conjunto[nom1]
				except:
					print "El conjunto",nom1,"no existe"
					nohuboerror=False
				try:
					con2=self.conjunto[nom2]
				except:
					print "El conjunto",nom2,"no existe"
					nohuboerror=False
				if nohuboerror:
					pe.subConjuntoPropio(con1,con2,nom1,nom2,"imp")
				pausa()
			elif opc=="5":
				nom1=raw_input("Primer conjunto: ")
				nom2=raw_input("Segundo conjunto: ")
				nohuboerror=True
				try:
					con1=self.conjunto[nom1]
				except:
					print "El conjunto",nom1,"no existe"
					nohuboerror=False
				try:
					con2=self.conjunto[nom2]
				except:
					print "El conjunto",nom2,"no existe"
					nohuboerror=False
				if nohuboerror:
					pe.disjunto(con1,con2,nom1,nom2,"imp")
				pausa()
			else:
				print "Opcion invalida"
				pausa()
	
	def ayuda(self):
		print "La teoria de conjuntos es bla bla bla, sirve para bla bla bla, este programa sirve para bla bla bla"
		print "Este programa solo es una practica de la teoria de conjuntos, hecho por un wanabbe normie grasoso de 16 :v"
		print "\nPrograma creado totalmemte por Luis Albizo 24-27/06/2016\nPresentar este codigo como prpyecto para tu escuela es un delito muy serio, no lo hagas inutil potque te hackeo el facebook y te rebiemto ok?"
		pausa()

menu=main(conjunto)

#Luis Albizo 27/06/16
