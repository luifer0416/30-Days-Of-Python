numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers=[i for i in numbers if i<1]
print(filtered_numbers)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattered_list=[z for x in list_of_lists for y in x for z in y]
print(flattered_list)


list_tuples=[]
for i in range(11):
	list_tuples.append((i,))
	for x in range(6):
		list_tuples[i]=list_tuples[i]+(i**x,)
	



list_tuples=[(i,)+tuple([i**x for x in range(6)]) for i in range(11) ]
print(list_tuples)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output=[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

countries_flattered=[[y[0].upper(),y[0][0:3].upper(),y[1].upper()] for x in countries for y in x]
print(countries_flattered)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output=['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

names_flattered=[str(i[0])+" "+str(i[1]) for x in names for i in x]
print(names_flattered)

slope=lambda x1,y1,x2,y2: (y2-y1)/(x2-x1)
print(slope(5,5,4,4))