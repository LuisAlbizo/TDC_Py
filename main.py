from conjuntos import *

class main:
	def __init__(self,uni):
		self.cc=uni
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
			print "Oocion 6: Salir de este submenu"
			opc=raw_input("\nEscoge tu opcion: ")
			limpiar()
			if opc=="6":
				pausa()
				break
			elif opc=="0":
				print "Proximamente :v...."
				pausa()
			elif opc=="1":
				nom1=raw_input("Primer conjunto: ")
				nom2=raw_input("Segundo conjunto: ")
				nohuboerror=True
				try:
					con1=self.cc[nom1]
				except:
					print "El conjunto",nom2,"no existe"
					nohuboerror=False
				try:
					con2=self.cc[nom2]
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
					con1=self.cc[nom1]
				except:
					print "El conjunto",nom1,"no existe"
					nohuboerror=False
				try:
					con2=self.cc[nom2]
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
					con1=self.cc[nom1]
				except:
					print "El conjunto",nom1,"no existe"
					nohuboerror=False
				try:
					con2=self.cc[nom2]
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
					con1=self.cc[nom1]
				except:
					print "El conjunto",nom1,"no existe"
					nohuboerror=False
				try:
					con2=self.cc[nom2]
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
					con1=self.cc[nom1]
				except:
					print "El conjunto",nom1,"no existe"
					nohuboerror=False
				try:
					con1=self.cc[nom2]
				except:
					print "El conjunto",nom2,"no existe"
					nohuboerror=False
				if nohuboerror:
					pe.disjunto(con1,con2,nom1,nom2,"imp")
				pausa()
			else:
				print "Opcion invalida"
				pausa()

menu=Menu()
menu.menuPertenencia(conjunto)

#Luis Albizo 27/06/16
