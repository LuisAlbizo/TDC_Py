from basicos import cortarDesde, pausa, limpiar, mostrarTexto

def redFloat(f):
	fl=str(f)
	flo=str(fl[cortarDesde(fl,".")+1:])
	flot=len(str(flo))
	cond=5*(10**(flot-1))
	floa=int(fl[:cortarDesde(fl,".")])
	if int(flo)>cond:
		return floa+1
	else:
		return floa

def numCoincidencias(li1,li2):
	l1=[]
	l2=li2
	for el in li1:
		l1.append(el)
	i=0
	for el in l1:
		ele=0
		while ele < len(l2):
			if el==l2[ele]:
				i+=1
				break
			ele+=1
	return i

def medirPorcentaje(p,num,t="float"):
	po=float(p)
	nume=float(num)
	por=(po/10.0)*(num/10.0)
	if t=="float":
		return float(por)
	elif t=="int":
		return int(por)

def juntarListas(l1,l2,p=0):
	lr=[]
	if p==0:
		for el in l1:
			i=0
			for ele in lr:
				if ele==el:
					i+=1
			if i==0:
				lr.append(el)
		for el in l2:
			i=0
			for ele in lr:
				if el==ele:
					i+=1
			if i==0:
				lr.append(el)
	return lr

def duplicarLista(lista):
	listaDuplicada=[]
	for el in lista:
		listaDuplicada.append(el)
	return listaDuplicada

def estaEn(que,donde):
	i=0
	for el in donde:
		if el==que:
			i+=1
	if i>0:
		return True
	else:
		return False

def eliminarDuplicados(lista):
	a=duplicarLista(lista)
	for el in range(0,len(lista)):
		b=duplicarLista(lista)
		b[el]="|>>i<<|"
		if estaEn(lista[el],b):
			a[el]=None
	c=[]
	for el in a:
		if el != None:
			c.append(el)
	return c
#La funcion eliminarDuplicados no funciona pero como solo la hice para solucionar otro error ya no la necesito :v (por ahora)
#print eliminarDuplicados([12,2,2,2,3,3])

#LuisAlbizo 25/06/16
