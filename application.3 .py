
"""
# Print type , 'İzmir ve İstanbul , İlk iki şehri ve son iki şehri 
cities = ('İzmir','Uşak','Ankara','Hatay','İstanbul')
print(type(cities))
print(cities[0])
print(cities[-1])
print(cities[:2])
print(cities[-2:])
"""

"""
#Print ismail , Print 8

new_tupple = ('İzmir',[28,'İsmail'],(2,4,8),100)
print(new_tupple[1][1])
print(new_tupple[2][-1])
"""


"""
#----STRİNG & TUPPLE

new_tupple = ('İstanbul',) #Sona virgül koyunca tupple oldu koymassak string olarak algıalr --
print(type(new_tupple))
"""

"""
# 4 Değerini 50'ye çevir     #----- Tupple'lar değişmez veri dizinidir---
# 1 Değerini 100'e çevir   # ------Tupple'ın içinde liste olduğu zaman onu değiştiribiliyoruz---

new_tupple = (4,8,[1,20])  
new_tupple[-1][0] = 100
print(new_tupple)
"""



"""
# İzmir ve Balıkesir'in Tupple olup olmadığını Kontrol et 

cities = ('İstanbul','Ankara','İzmir')
print('İzmir'in cities)
print('Balıkesir'in cities)
"""




"""
# Aynı değerleri Teke İndirelimm
# Set Veya Tupple
 # Set olarak istemiyorum derse

new_tupple = ('S','İzmir',28,'Ankara','S','İzmir')
new_set = set(new_tupple)
new_tupple2 = tuple(new_set)
print(new_tupple2) 
print(type(new_tupple2))
"""



"""
# İsmini ekleyip Liste yapısına Çevir
# --------- () Normal parantez kullanırsak tupple oluyor { } süslü parantezde ise set yapısı oluyor------
#--------------Tupple yapılarına ekleme yapılamıyor---

new_set = {'Ali','Fatma','Çağlar','Berrin'}
print(type(new_set))
new_set.add('İsmail')
new_list = list(new_set)
print(new_list)
"""



# asdfahhhjdjkadldsldl kelimesinde tüm harfleri teke indir ve set halinde yazdır 

new_string = 'asdfahhhjdjkadldsldl'

new_set = { harf for harf in new_string }
print(new_set)

