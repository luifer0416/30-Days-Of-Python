#1
age=27
height=1.75
complejo=4+5j

#base=float(input())
#heigh=float(input())
#area=0.5*base*heigh
#print("El area es",area)

#print("ingrese lado a")
#side_a=float(input())
#print("ingrese lado b")
#side_b=float(input())
#print("ingrese lado c")
#side_c=float(input())
#perimetro=side_a+side_b+side_c
#print("el perimetro es",perimetro)

#print("ingrese lenght")
#lenght=float(input())
#print("ingrese widht")
#width=float(input())
#area=lenght*width
#perimetro=2*(lenght+width)
#print("el area es",area,"el perimetro es",perimetro)

#print("ingrese radious")
#raidious=float(input())
#area=3.14*raidious**2
#circumference=2*3.14*raidious
#print("el area es",area,"la circunferencia es",circumference)

y="2x-2"
m=""
for z in y:
	if z!="x":
		m=m+z
	else:
		break
m=float(m)
print(m)
x=""
y_intercept=""
for z in y:
	if x=="-" or x=="+":
		y_intercept=float(x+y_intercept+z)
	x=z

print(y_intercept)
y_intercept=1

p1=(2,2)
p2=(6,10)
m2=(p2[1]-p1[1])/(p2[0]-p1[0])
print(m2)
distance=((p2[1]-p1[1])+(p2[0]-p1[0]))**0.5
print("m1 y m2 son iguales",m==m2)

for x in range(-100,100):
	y=x**2+6*x+9
	if y==0:
		print("Para que y sea 0 x es igual a",x)
		break

print(len("phyton") is not len("dragon"))
print("on" in ("phyton" and "dragon"))
print("on" in "I hope this course is not full of jargon")
print("on" not in ("phyton" and "dragon"))
print(type(str(float(len("phyton")))))

#for x in range(-100,100):
#	if x%2==0:
#		print(x,"es par")

#print(7//3==int(2.7))
#print(type(10)==type("10"))
#print(10==int(9.8))

#print("ingrese horas")
#hours=float(input())
#print("pago por hora")
#rate=float(input())
#pay=hours*rate
#print("La paga es", pay)

#print("ingrese años vividos")
#years=float(input())
#segundos=(years*365*24*60*60)
#print("Usted ha vivido", segundos, "segundos")
line=""
for x in range(1,6):
	line=str(x)+" "+"1"
	z=1
	y=1
	while z<4:
		y=x*y
		line=line+" "+str(y)
		z+=1
	print(line)
