import requests
import pprint
import json

url='https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
print(response)
print(response.status_code)
cats=response.json()
weights=[x["weight"]["metric"].split(" - ") for x in cats]
weights_avg=[(int(w[0])+int(w[1]))/2 for w in weights]


life=[x["life_span"].split(" - ") for x in cats]
life_avg=[(int(l[0])+int(l[1]))/2 for l in life]



def min_max(lista):
	lista.sort()
	min=lista[0]
	max=lista[len(lista)-1]
	return min,max

def mean(lista):
	total=0
	for x in lista:
		total+=x
	mean=total/len(lista)
	return mean


def median(lista):
	lista.sort()
	if len(lista)%2!=0:
		mediana=lista[len(lista)//2]
	else:
		mediana=(lista[len(lista)//2-1]+lista[len(lista)//2])/2
	return mediana



def variance(lista):
	mediana=mean(lista)
	numerador=0
	for x in range(len(lista)):
		numerador+=(lista[x]-mediana)**2
	variance=numerador/len(lista)
	return variance


def cacl_desv_std(lista):
	desv_std=variance(lista)**(1/2)
	return desv_std

print(min_max(weights_avg))
print(mean(weights_avg))
print(median(weights_avg))
print(cacl_desv_std(weights_avg))

print(min_max(life_avg))
print(mean(life_avg))
print(median(life_avg))
print(cacl_desv_std(life_avg))


cats_breeds=[{"breeds":c["name"],"country":c["origin"]}for c in cats]
cats_country=set([c["origin"]for c in cats])
cats_frequency=[{"country":c,"breeds":[g["breeds"] for g in cats_breeds if g["country"]==c]}for c in cats_country]
sorted_by_breeds = sorted(cats_frequency, key=lambda x: len(x['breeds']),reverse=True)
print(sorted_by_breeds)
#cats_breeed_country=[{"country":c,"breeds":[b for b in cats_breeds if b["country"]==] for c in cats_country ]
#print(cats_breeds)

