dog={}
dog["Name"]="Mali"
dog["breed"]="Shit zhu"
dog["legs"]=4
dog["age"]=2
print(dog)

student={"first name":"Luis","Last name":"Ahumedo","gender":"Male","marital status":"single","skills":["Python","Excel","LOL"],"Country":"Colombia","City":"Bogota","Adres":{"street":"Avenida cali","Bariio":"florencia"}}
print(student)
print(len(student))
print(student["skills"])
print(type(student["skills"]))
student["skills"].append("Wild rift")
student["skills"].append("Logical games")
print(student["skills"])

keys=student.keys()
print(keys)
values=student.values()
print(values)
dct=student.items()
print(dct)
del  student["first name"]
print(student)
student.popitem()
print(student)