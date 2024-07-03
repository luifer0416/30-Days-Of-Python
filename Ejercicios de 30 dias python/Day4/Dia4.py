a="Thirty"
b="Days"
c="Of"
d="Python"

s=a+" "+b+" "+c+" "+d
print(s)

a="Coding"
b="For"
c="All"

s=a+" "+b+" "+c
print(s)

company=s
print(s)
print(len(s))

print(s.upper())
print(s.lower())

format1=s.capitalize()
format2=format1.title()
format3=format2.swapcase()

print(format3)

print(s.strip("Coding"))
print(s.find("Coding"))
print(s.replace("Coding","Python"))
print(s.replace("All","Every one"))
print(s.split(" "))

aplicaciones="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(aplicaciones.split(","))
print(s[0])
print(s[len(s)-1])
print(s[10])

acronimo=""
for x in s:
	if x.isupper():
		acronimo=acronimo+x+"."
print(acronimo)

print(s.index("C"))
print(s.index("F"))
print(s.rindex("l"))
sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.find("because"))
sentence= 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rfind("because"))
sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.replace("because",""))
sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.index("because"))
sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.replace("because because because",""))

print(s.startswith("Coding"))
print(s.endswith("Coding"))

sentence='   Coding For All      ' 
print(sentence.strip("ll"))

s1,s2="30DaysOfPython","thirty_days_of_python"
print(s1.isidentifier(),s2.isidentifier())

librerias=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(librerias))

print("I am enjoying this challenge.\n I just wonder what is next. ")
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
radius=10
area=3.14*radius**2

print(f"The area of a circle with radius {radius} is {area} meters square")

print(f"{8}+{6}={8+6}")
print(f"{8}-{6}={8-6}")
print(f"{8}*{6}={8*6}")
print(f"{8}/{6}={8/6}")
print(f"{8}%{6}={8%6}")
print(f"{8}//{6}={8//6}")
print(f"{8}**{6}={8**6}")
