def numCoincidencias(li1,li2):
	l1=li1
	l2=[]
	for el in li2:
		l2.append(el)
	i=0
	for el in l1:
		for ele in range(0,len(l2)):
			if el==l2[ele]:
				i+=1
				l2[ele]="|>>i<<|"
	return i

def medirPorcentaje(p,num,t="int"):
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
