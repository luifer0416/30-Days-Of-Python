import requests
import json
from bs4 import BeautifulSoup
import re

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
response = requests.get(url)
content = response.content

wikipedia =BeautifulSoup(content, 'html.parser')

presidentes_data=wikipedia.find("table")



headers_list=[x.get_text(strip=True) for x in presidentes_data.find('tr') if x.get_text(strip=True)!='']
print(headers_list)

presidentes_lista=[]
body=presidentes_data.find("tbody")
presidentes=body.find_all("tr")


for presi in presidentes[1:]:
	iwant=presi.find_all(["th","td"])
	presi_information={}
	
	for index,rest in enumerate(iwant):
		if index==4:
			continue
		if index>4:
			index-=1
		if index==1:
			rest=rest.find("a")
			link=rest.get('href')
			presi_information[headers_list[index]]=link
		else:
			presi_information[headers_list[index]]=rest.get_text(strip=True)
	presidentes_lista.append(presi_information)

print(json.dumps(presidentes_lista,indent=4))
with open('./presidentes_wikipedia.txt','w') as f:
    f.write(json.dumps(presidentes_lista,indent=4))
