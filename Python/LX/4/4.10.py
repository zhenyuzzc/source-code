meishis=['liulanpzz','zhizunpzz','xiaweiyipzz','baishu','qiaokeli']
print('"The first three items in the list are:"')
print(meishis[:3])
print()
print('"Three items from the middle of =the list are:"')
print(meishis[1:4])
print(meishis[-3:])
print()

#练习4-11
friend_pizzas=meishis[:]
meishis.append('huasheng')
friend_pizzas.append('mala')
print('"My favorite pizzas are:"')
for valve in meishis:
    print(valve)
print()
print('"My friend’s favorite pizzas are:"')
for valve in friend_pizzas:
    print(valve)
