
import re
#Ejercicios lvl 1
"""
def count_text(documento):
	documento=documento.read()
	words=documento.split()
	num_words=len(words)
	lineas= documento.splitlines()
	num_lineas=len(lineas)
	
	return num_lineas, num_words

with open('./data/obama_speech.txt') as f:
	print(count_text(f))

with open('./data/michelle_obama_speech.txt') as f:
	print(count_text(f))

with open('./data/donald_speech.txt') as f:
	print(count_text(f))



import json

def most_spoken_languages(countries_data,most_spoken=10):
	lenguajes=[]
	for data in countries_data:
		lenguajes.append(data["languages"])
	
	lenguajes=[i for idioma in lenguajes for i in idioma]	
	lenguajes_st=set(lenguajes)

	popular_languages=[]
	for idioma in lenguajes_st:
		popular_languages.append(((lenguajes.count(idioma)),idioma))
	popular_languages.sort(reverse=True)
	popular_languages=popular_languages[0:most_spoken]

	return popular_languages

def most_populated_countries(countries_data,most=10):
	populated_countris=[{"country":country["name"],"population":country["population"]} for country in countries_data]
	populated_countris = sorted(populated_countris, key=lambda x: x['population'],reverse=True)
	return populated_countris[0:most]

with open('./data/countries_data.json','r', encoding='utf-8') as f:
	f = json.loads(f.read())
	print(most_spoken_languages(f))
	print(most_populated_countries(f,3))

def extract_email(documento):
	lineas=documento.read()
	regix_pattern='Author: '+r'.+'
	email=list(set((re.findall(regix_pattern,lineas))))
	for x in email:
		email[email.index(x)]=re.sub("Author: ","",x)
		
	return (sorted(email))

with open('./data/email_exchanges_big.txt') as f:
	print(extract_email(f))


def find_most_common_words(texto,most=10):
	most_words=[]
	if type(texto)==str:
		pass
	else:
		texto=texto.read()
	regix_pattern=r"[w]+"
	words_unique=set(re.findall(regix_pattern,texto))
	for x in words_unique:
		if len(x)>1:
			most_words.append((texto.count(x),x))
	return (sorted(most_words,reverse=True))[0:most]

prueba="Hola como como estas, yo bien y tu."
print(find_most_common_words(prueba))

with open('./data/obama_speech.txt') as f:
	print(find_most_common_words(f))

"""
stop_words = ['i',"us",'me','my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up','down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]


def clean_text(texto):
	texto=texto.read()
	regix_pattern=r'[^A-Za-z]'
	clean=re.sub(regix_pattern," ",texto)
	clean=clean.split()
	def remove_support_words():
		remove=set([x.lower() for x in clean if x.lower() not in stop_words])
		return remove
	return remove_support_words

def check_text_similarity(textA,textB):
	textA=clean_text(textA)()
	textB=clean_text(textB)()
	similarity=len([palabra for palabra in textA if palabra in textB])
	return similarity


with open('./data/michelle_obama_speech.txt') as fa:
	with open('./data/melina_trump_speech.txt') as fb:
		print(check_text_similarity(fa,fb))

import csv


def count_csv(csv):
	count_p=0
	count_j=0
	count_j_not=0
	for row in csv:
		row=" ".join(row)
		if re.search(r"\bPython\b", row, re.I):
			count_p += 1
		if re.search(r"\bJavaScript\b", row, re.I):
			count_j += 1
		if re.search(r"\bJava\b(?!Script)", row, re.I):
			count_j_not += 1
	return count_p,count_j,count_j_not

		




with open('./data/hacker_news.csv') as f:
	csv_reader = csv.reader(f, delimiter=',')
	print(count_csv(csv_reader))