from basicos import cortarDesde

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

def duplicarLista(lista):
	listaDuplicada=[]
	for el in lista:
		listaDuplicada.append(el)
	return listaDuplicada

def estaEn(que,donde):
	i=False
	for el in donde:
		if el==que:
			i=True
	if i:
		return True
	else:
		return False

def eliminarDuplicados(lista):
	lr=[]
	for el in lista:
		i=0
		for ele in lr:
			if ele==el:
				i+=1
		if i==0:
			lr.append(el)
	return lr
	
def juntarListas(l1,l2):
	return eliminarDuplicados(l1+l2)

def elementosComunes(l1,l2):
	a=eliminarDuplicados(l1)
	b=eliminarDuplicados(l2)
	comunes=[]
	for el in a:
		if estaEn(el,b):
			comunes.append(el)
	return comunes

def quitar(li1,l2):
	l1=eliminarDuplicados(duplicarLista(li1))
	for i in range(0,len(l1)):
		if estaEn(l1[i],l2):
			l1[i]=None
	dif=[]
	for el in l1:
		if el != None:
			dif.append(el)
	return dif

#LuisAlbizo 25/06/16
