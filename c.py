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


#LuisAlbizo 25/06/16
