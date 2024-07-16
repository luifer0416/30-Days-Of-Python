class Statistics:
	def __init__(self,lista):
		self.lista=lista

	
	def count(self):
		return len(self.lista)

	def suma(self):
		suma=0
		for s in self.lista:
			suma+=s
		return suma


	def mini(self):
		self.lista.sort()
		minimo=self.lista[0]
		return minimo

	def maxi(self):
		self.lista.sort()
		maximo=self.lista[len(self.lista)-1]
		return maximo

	def range(self):
		rango=self.maxi()-self.mini()
		return rango


	def mean(self):
		total=0
		for x in self.lista:
			total+=x
		mean=total/len(self.lista)
		return mean


	def median(self):
		self.lista.sort()
		if len(self.lista)%2!=0:
			mediana=self.lista[len(self.lista)//2]
		else:
			mediana=(self.lista[len(self.lista)//2-1]+self.lista[len(self.lista)//2])/2
		return mediana

	def mode(self):
		count=0
		for x in self.lista:
			if self.lista.count(x) > count:
				count=self.lista.count(x)
				moda=x
		return {"moda":moda,"count":count}
	def variance(self):
		mediana=self.mean()
		numerador=0
		for x in range(len(self.lista)):
			numerador+=(self.lista[x]-mediana)**2
		variance=numerador/len(self.lista)
		return variance


	def std(self):
		desv_std=self.variance()**(1/2)
		return desv_std


ages=Statistics([31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26])
print(ages.suma())
print(ages.mini())
print(ages.maxi())
print(ages.range())
print(ages.mean())
print(ages.median())
print(ages.mode())
print(ages.std())
print(ages.variance())

