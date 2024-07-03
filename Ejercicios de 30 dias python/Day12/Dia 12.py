

from random import randint,shuffle
from string import ascii_letters, digits



def random_user_id():
	letters_digits=list(ascii_letters)+list(digits)
	id=""
	for x in range(6):
		id+=str(letters_digits[randint(0,len(letters_digits)-1)])
	return id

print(random_user_id())
"""
def user_id_gen_by_user():
	letters_digits=list(ascii_letters)+list(digits)
	num_character=input("Ingrese numero de caracteres: ")
	num_id=input("ingrese numero de id: ")
	for x in range(int(num_id)):
		id=""
		for y in range(int(num_character)):
			id+=str(letters_digits[randint(0,len(letters_digits)-1)])
		print(id)

print(user_id_gen_by_user())
"""
def rgb_color():
	rgb=[]
	for x in range(3):
		rgb.append(randint(0,255))
	rgb=tuple(rgb)
	return rgb

def list_of_hexa (n):
	list_hexa=list(ascii_letters)[0:6]+list(digits)[0:10]
	colors=[]
	for x in range(n):
		hexa="#"
		for y in range(6):
			hexa+=str(list_hexa[randint(0,len(list_hexa)-1)])
		colors.append(hexa)
	return colors

def list_rgb_color(n):
	colors=[]
	for x in range(n):
		rgb=[]
		for x in range(3):
			rgb.append(randint(0,255))
		rgb="rgb"+str(tuple(rgb))
		colors.append(rgb)
	return colors

def generate_colors(color,cantidad):
	if color=="hexa":
		colors=list_of_hexa(cantidad)
		return colors
	else:
		colors=list_rgb_color(cantidad)
		return colors

print(list_of_hexa(5))
print(list_rgb_color(5))
print(generate_colors("rgb",6))

def shuffle_list(x):
	shuffle=[]
	while len(shuffle)<len(x):
		agregar=x[randint(0,len(x)-1)]
		if agregar in shuffle:
			pass
		else:
			shuffle.append(agregar)
	return shuffle

print(shuffle_list([9,8,7,6,5,4,3,2,1,0]))

def array_seven():
	array=[]
	while len(array)<7:
		agregar=randint(0,9)
		if agregar in array:
			pass
		else:
			array.append(agregar)
	return array

print(array_seven())
