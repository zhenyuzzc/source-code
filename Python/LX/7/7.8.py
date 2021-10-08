sandwich_orders = ['yanmaipeigen','jingqiangyu','jidanhuotui','tudouni']
finished_sandwiches = []
# for循环遍历列表
for value in sandwich_orders:
    print(f"I made your tuna {value}")
print()

# while循环遍历列表
while sandwich_orders:
    i = 0
    finished_sandwiche = sandwich_orders.pop(i)
    print(f"I made your tuna {finished_sandwiche}")
    finished_sandwiches.append(finished_sandwiche)
    i += 1
print(finished_sandwiches)
