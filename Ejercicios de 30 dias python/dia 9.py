"""
#Exercise lvl 1
age=int((input("Ingresa tu edad: ")))
if age>=18:
	print("You are old enough to drive")
else:
	wait=18-age
	print(f"You need {wait} more years to learn to drive")
"""
#Exercise lvl 2

"""
my_age=27
your_age=int((input("Ingresa tu edad: ")))

if my_age-your_age<0:
	if my_age-your_age==-1:
		print(f"you are {abs(my_age-your_age)} years older than me")
	else:
		print(f"you are {abs(my_age-your_age)} year older than me")
elif my_age-your_age>0:
	if my_age-your_age==-1:
		print(f"I am {abs(my_age-your_age)} years older than you")
	else:
		print(f"I am {abs(my_age-your_age)} year older than you")
else:
	print("We have the same years old")
"""

"""
a=int((input("Ingresa número a: ")))
b=int((input("Ingresa número b: ")))


if a>b:
	print(f"{a} is greater than {b}")
elif b<a:
	print(f"{a} is smaller than {b}")
else:
	print(f"{a} is equal than {b}")
"""
#Exercise level 2

"""
scores=float(input("Ingresa la nota: " ))
if scores>=80:
	print("The grade of studen is A")
elif scores>=70:
	print("The grade of studen is B")
elif scores>=60:
	print("The grade of studen is C")
elif scores>=50:
	print("The grade of studen is D")
else:
	print("The grade of studen is F")
"""
"""
month=(input("Ingresa el mes: " ))

if month=="September" or month=="October" or month=="November":
	print("The season is Autumn")
elif month=="December" or month=="January" or month=="February":
	print("The season is winter")
elif month=="March" or month=="April" or month=="May":
	print("The season is Spring")
else:
	print("The season is Summer")
"""
"""
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit=(input("Ingrese una furta: " ))

if fruit in fruits:
	print('That fruit already exist in the list')
else:
	fruits.append(fruit)
	print(fruits)
"""
#Exercvise lvl 3
person={
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_marred': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
'street': 'Space street',
'zipcode': '02210'
}
}

if "skills" in person:
	print(person["skills"][len(person["skills"])//2])

if "skills" in person:
	if "Python" in person["skills"]:
		print(person["skills"][person["skills"].index("Python")])

if len(person["skills"])==2 and "JavaScript" in person["skills"] and "React" in person["skills"]:
	print('He is a front end developer')
elif len(person["skills"])>2:
	if "Node" in person["skills"] and "Python" in person["skills"] and "MongoDB" in person["skills"]:
		print('He is a backend developer')
	if "Node" in person["skills"] and "React" in person["skills"] and "MongoDB" in person["skills"]:
		print('He is a fullstack developer')
else:
	print('unknown title')

if person["is_marred"] and person["country"]=="Finland":
	print(f"{person["first_name"]} {person["last_name"]} live in {person["country"]}, He is married")
