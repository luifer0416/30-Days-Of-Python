import re
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
regex_patterns=r'[A-Za-z]+'
find_pattern=set(re.findall(regex_patterns,paragraph))
most_frequent=sorted([(paragraph.count(palabra),palabra)for palabra in find_pattern],reverse=True)
print(find_pattern)
print(most_frequent)

text="The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."
regex_patterns=r'-?\d+'
find_pattern=re.findall(regex_patterns,text)
posiciones=sorted([int(num) for num in find_pattern])
distancia=posiciones[len(posiciones)-1]-posiciones[0]
print(find_pattern)
print(posiciones)
print(distancia)

#Excercise lvl2
def is_valid_variable(text):
    regex_patterns=r'^[^A-za-z]|[^A-Za-z0-9_]'
    find=re.findall(regex_patterns,text)
    if len(find)>0:
        return False
    return True

valid=is_valid_variable('first_n5ame') # True
print(valid)
valid=is_valid_variable('first-name') # False
print(valid)
valid=is_valid_variable('1first_name') # False
print(valid)
valid=is_valid_variable('firstname') # True
print(valid)

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

regex_patterns=r'[^A-Za-z0-9 .]'
clean_text=re.sub(regex_patterns,"",sentence)
regex_patterns=r'[A-Za-z]+'
find_pattern=set(re.findall(regex_patterns,clean_text))
print(clean_text)
most_frequent=sorted([(clean_text.count(palabra+" "),palabra)for palabra in find_pattern],reverse=True)[0:3]
print(most_frequent)