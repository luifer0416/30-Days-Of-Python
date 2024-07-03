# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add("Twitter")
print(it_companies)
it_companies.update(["Nvidia","Intel","UPS"])
print(it_companies)
it_companies.remove("Oracle")
#Discard() don't produce error when a item is not found in a list


#Level 2
C=A.union(B)
print(C)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(B.isdisjoint(A))
#A.update(B)
#B.update(A)
print(A)
print(B)
print(A.symmetric_difference(B))
del A 
del B 

#Level 3
age_lt=list(age)
print(len(age),len(age_lt)) #Equals

"""
Strings are characters inmutable and indexing
List are set of any type of data mutable and indexing
tuple are set of any type of datta immutable and indexing
set is a set of the same data type no indexing and inmmutable
"""
frase="I am a teacher and I love to inspire and teach people."
frase_lt=frase.split()
print(len(frase_lt))
frase=set(frase.split())
print(frase)
print(len(frase))