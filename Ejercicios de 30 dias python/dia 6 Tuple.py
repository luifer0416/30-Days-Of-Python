empty=tuple()
sisters=("Laura","Olga")
brothers=("Ariel","Iker")
siblings=sisters+brothers
print(siblings)
print(len(siblings))
siblings=list(siblings)
parents=["Patricia","Ariel"]
family_members=siblings+parents
print(tuple(family_members))

sis1,sis2,bro1,bro2,*parents=family_members
print(sis1)
print(sis2)
print(bro1)
print(bro2)
print(parents)

fruits=("Banana","Coco","Mango","Fresa")
vegetables=("Brocoli","Sukuni","Tomate","Cebolla")
animal=("Perro","Gato","Loro","Rata")
food_stuff_tp=fruits+vegetables+animal
print(food_stuff_tp)
food_stuff_lt=list(food_stuff_tp)
middle=food_stuff_tp[0:(len(food_stuff_tp)//2)]
print(middle)
new_lt=food_stuff_tp[3:(len(food_stuff_tp)-3)]
print(new_lt)
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)