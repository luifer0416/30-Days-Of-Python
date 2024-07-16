
empty=list()
print(empty)
varios_items=list("Hola mundo")
print(varios_items)
print(len(varios_items))
print(varios_items[0])
print(varios_items[(len(varios_items)-1)//2])
print(varios_items[len(varios_items)-1])
mixed_data=["luis",27,1.75,"Soltero","Calle siempre viva 123"]
it_comapnies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(it_comapnies)
print(len(it_comapnies))
print(it_comapnies[0])
print(it_comapnies[(len(it_comapnies)-1)//2])
print(it_comapnies[len(it_comapnies)-1])
it_comapnies[0]="TAC"
print(it_comapnies)
it_comapnies.append("IT")
print(it_comapnies)
it_comapnies[len(it_comapnies):]=["otra"]
print(it_comapnies)
it_comapnies.insert((len(it_comapnies)-1)//2,"Mid Company")
print(it_comapnies)
it_comapnies[1]=it_comapnies[1].upper()
print(it_comapnies)
it_comapnies.extend("$")
print(it_comapnies)
print("Microsoft" in it_comapnies)
it_comapnies.sort()
print(it_comapnies)
it_comapnies.sort(reverse=True)
print(it_comapnies)
del it_comapnies[0:3]
print(it_comapnies)
del it_comapnies[len(it_comapnies)-3:]
print(it_comapnies)
del it_comapnies[(len(it_comapnies)-1)//2]
print(it_comapnies)
del it_comapnies[0]
print(it_comapnies)
del it_comapnies[(len(it_comapnies)-1)]
print(it_comapnies)
it_comapnies.clear()
print(it_comapnies)
del it_comapnies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
unidos=front_end+back_end
print(unidos)
unidos_copia=unidos.copy()
print(unidos_copia)
unidos_copia.insert(unidos_copia.index("Redux")+1,"Python")
unidos_copia.insert(unidos_copia.index("Python")+1,"SQL")
print(unidos_copia)

#Exercise lvl 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
minimo=ages[0]
maximo=ages[len(ages)-1]
print(ages, minimo,maximo)
average=sum(ages)/len(ages)
print(average)
rango=max(ages)-min(ages)
print(rango)
rango=ages[len(ages)-1]-ages[0]
print(rango)
compare=abs(min(ages)-average)==abs(max(ages)-average)
print(compare)


countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

middle=(len(countries)-1)//2
print(middle)
first_half_countries=countries[:middle]
second_half_countries=countries[middle:]

print(first_half_countries)
print("Aqui la mitad")
print(second_half_countries)

paises=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
primer_pais,segundo_pais,tercer_pais,*scandic=paises
print(primer_pais)
print(segundo_pais)
print(tercer_pais)
print(scandic)
