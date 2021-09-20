sandwich_orders = ['yanmaipeigen','pastrami','jingqiangyu','pastrami','jidanhuotui','pastrami','tudouni']
print("五香徐牛肉已经卖完了（pastrami）")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("只有这些了：")
print(sandwich_orders)

