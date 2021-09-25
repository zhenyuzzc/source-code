from random import choices
sz = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e']
i = 1
while i <= 5:
    number= choices(sz)
    i += 1
    print(number)
print("如果您彩票是这5个数就中奖了")