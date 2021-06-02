"""
# Boş liste , tuple , set ve dictionaries oluştur 

list_1 = []  #Boş liste
print(type(list_1))

#Tupple
tuple_1 = () # Normal parantez ile
tuple_2 = tuple()
print(type(tuple_1))
print(type(tuple_2))

#Set 
set_2 = set()
print(type(set_2))

#Dictiomnaries
dict1 = {} #süsülü parantez
dict2 = dict()
print(type(dict1))
print(type(dict2))
"""


"""
# Değeri sayı olan 3 elemanlı bir dictionary oluştur , 2.sayıyı ve sayıların ortalamasını çıkar

Friend = {'Fatma': 19, 'Ebru': 18, 'Pınar': 17}

print(Friend['Ebru'])

print(sum(Friend.values()) / len(Friend) )
"""

"""
# 2 okul arkadaşı ve numaralardan oluşan bir dict. oluştur , başka bir arkadaşını ekle , ekli olan arkadaşı sil , Uptade ile bir arkadaşın numarasını değiştir ve yeni arkadaş ekle

friends = {'Fatma' : 345,'Ebru': 312,}
friends['Eren'] = 214
print(friends)
del friends['Eren']
print(friends)

friends.update({'Fatma': 125, 'İsmail': 19})
print(friends)
"""

"""
# my_dict  = {'add_numbers': [1,2,3] }
# Yukaridaki dictionary yapısında bulunan tüm elemanların karesini alalım aynı dictionary yapısını uptade edelim


my_dict  = {'add_numbers': [1,2,3] }
my_dict['add_numbers'] = [my_dict['add_numbers'][0] ** 2, my_dict['add_numbers'][1] ** 2, my_dict['add_numbers'][2] ** 2, ]
print(my_dict)
"""

"""
# my_dict2 = {'Even_numbers': [2,4,6,8,12,14,16]}
# Yukaridaki dictionary yapısında bulunan tüm elemanların karesini alalım aynı dictionary yapısını uptade edelim , ---Bu kez for döngüsü kullanalım--

my_dict2 = {'Even_numbers': [2,4,6,8,12,14,16]}

for x in my_dict2.values():
    my_list = []
    for y in x:
        my_list.append(y**2)
my_dict2['Even_numbers'] = my_list     

print(my_dict2)
"""


"""
# Keylerden liste oluştur , value 'lardan liste oluştur ve valuelar toplamını yazdır

my_friend = {'İsmail' : 19 , 'Fatma': 18 , 'Ebru': 20}
my_key_list = []
my_value_list= []

for k, v in my_friend.items():
    my_key_list.append(k)
    my_value_list.append(v)

print(my_key_list)
print(my_value_list)
print(sum(my_value_list))

"""

# Dictionary comprehension ile 1'den 10'a kadar olan sayılar , sayıları key , kareleri value olacak şekilde tek satırdı oluştur

number = { x: x**2 for x in range(1, 11)}
print(number)