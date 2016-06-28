from os import system
def limpiar():
	system("clear")
def pausa(m="Presione enter"):
	raw_input(m)
	limpiar()
abc="abcdefghijklmnopqrstuvwxyz"
ABC=abc.upper()
abc=abc+ABC
def cortarDesde(b,c):
#Funcion que retorna el indice en el que se emcuentra una coincidencia
#B es la cadena o lista a inspeccionar y C es la coincidencia que tiene que encontrar
#Cuando encuentre la coincidencia retornara el indice en el que se encuentra
	i=0
	while True:
		if b[i]==c:
			break
		else:
			i+=1
	return i

def cabecera(cabeza):
	titulo=cabeza[0:cortarDesde(cabeza,":")]
	i=0
	while True:
		if cabeza[i] == "T" and cabeza[i+1]=="e" and cabeza[i+2] == "m" and cabeza[i+3] == "a":
			numTema=cabeza[i:i+6]
			tema = cabeza[i+7:-2]
		if i==len(cabeza)-1:
			break
		i+=1
	return {"titulo":titulo,"numTema":numTema,"tema":tema}

def itsa(w, m):
#Funcion que retorna true si m es del tipo que se quiere saber
#int para numeros(no decimales)
#let para letras, todas las letras del abecedario en may y min excepto la... no la puedo escrihir en este ide :"v
#sig para signos - o +
	if w == "int":
		try: 
			int(m)
			return True
		except:
			return False
	elif w=="let":
		i=0
		for el in abc:
			if el == m:
				i+=1
		if i>0:
			return True
		else:
			return False
	elif w=="sig":
		if m == "+" or m == "-":
			return True
		else: 
			return False
	elif w=="exp":
		if m == "*":
			return True
		else:
			return False
