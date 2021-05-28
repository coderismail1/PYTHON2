"""
#İKİNCİ VE SON LİSTE ELEMANININ ÇIKTISINI BÜYÜK HARFLE ALIN
cities = ['Uşak', 'Manisa','İzmir','Ankara','İSTANBUL']
print(cities[1].upper())
print(cities[-1].upper())
"""


"""
# İzmir ve Ankara elemanlarının çıktısını al,
# İlk iki elemanın çıktısını al,
# Son iki  elemanın çıktısını al,

cities = ['Uşak', 'Manisa','İzmir','Ankara','İSTANBUL']
print(cities[2:4])
print(cities[:2])
print(cities[-2:])
"""


"""
# Nested list kullanılmış ,
# Son elemanın çıktısını len yardımı ile al ,

cities = ['Uşak', 'Manisa',['İzmir','Ankara'],'İstanbul','Antalya']

print(cities[2])
print(cities[len(cities)-1])
"""


"""
#Liste uzunluğunu göster 
# Listeye Afyon ili'ni ekle 
# Adıyaman İli'ni ekle 2.yol 

cities = ['Uşak', 'Manisa','İzmir','Ankara','İSTANBUL']

print(len(cities))
cities.append('Afyon')
print(cities)

cities[len(cities):] = ['Adıyaman']
print(cities)
"""


"""
# İnsert ile Afyon İli'ni liste başına ekle,
# insert ile Adıyaman İli'ni liste sonuna ekle ,

cities = ['Uşak', 'Manisa','İzmir','Ankara','İSTANBUL']

cities.insert(0,'Afyon')
print(cities)
cities.insert(len(cities), 'Adıyaman')
print(cities)
"""


"""
# Del ile Manisa elemanını Kaldır ,
# Remove ile İzmir elemanını Kaldır ,

cities = ['Uşak', 'Manisa','İzmir','Ankara','İSTANBUL']

del cities[1]
print(cities)

cities.remove('İzmir')
print(cities)
"""


"""
# Listeyi artacak ve azalacak şekile Sırala..

numbers = [0,5,6,4,2,55,85,36,87,25,3,10]

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)
"""



"""
# İçteki listelerin son elemanları ile bir liste oluşturalım

cities = [['Uşak', 'Manisa'],['İzmir','Ankara'],['İSTANBUL','Afyon']]
cities_2 = []
 
for city in cities:
    cities_2.append(city[-1])
print(cities_2)

# -----UZUN YOL------
cities_2 = []
cities_2.append(cities[0][-1])
cities_2.append(cities[1][-1])
cities_2.append(cities[2][-1])
print(cities_2)
"""

"""
# 1'den 10'a kadar olan sayıların Karelerinden list Oluşturalım 
# Aynı işlemi List Comprehension ile yapalım .

squares = []
for num in range(1,11):
    squares.append(num**2)
print(squares)

# List Comprehension
squares = [num**2 for num in range(1,11)]
print(squares)
"""