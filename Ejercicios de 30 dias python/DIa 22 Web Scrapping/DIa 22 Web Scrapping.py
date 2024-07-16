import requests
import json
from bs4 import BeautifulSoup
import re

#Ejercicio 1
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
content = response.content

soup =BeautifulSoup(content, 'html.parser')

categorias=[cat.get_text(strip=True) for cat in soup.find_all('h4','stat-group-title') ]

data_dict=[{"categoria":x} for x in categorias]

	

all_data=soup.find("div",class_='content-container')


for i in range(3,6,2):
	datos=all_data.find('div',class_=f"bu-stat-list bu-stat-count-{i}")
	claves=[]
	valores=[]
	
	for clave in datos.find_all('h3','bu-stat-title'):
		claves.append(clave.get_text(strip=True))
	for valor in datos.find_all('span',class_='bu-stat-value-field'):
		if re.match(r'[A-Za-z0-9]+',valor.get_text(strip=True)) and len(valor.get_text(strip=True))>1:
			valores.append(valor.get_text(strip=True))
	dicc=dict(zip(claves,valores))
	if i==5:
		data_dict[2].update(dicc)
	else:
		data_dict[0].update(dicc)

sections=all_data.find_all("section",class_="stat-section")


for index,section in enumerate(sections):
	datos=section.find_all("li")
	
	#print(section)
	claves=[]
	valores=[]
	for item in datos:
		clave=item.find("span",class_="stat-label").text.strip()
		valor=item.find("span",class_="stat-figure")
		val=valor.text.strip()
		if index==0:
			data_dict[1][clave]=val
		else:
			data_dict[3][clave]=val


print(data_dict)





with open('./DIa 22 Web Scrapping/web_scrapping.txt','w') as f:
    f.write(json.dumps(data_dict,indent=4))







