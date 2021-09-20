mx = {}
i = True
while i:
    name = input("输入你的名字： ")
    dz = input("输入你梦想去到的地方： ")
    mx[name] = dz
    n = input("是否还有人填写梦想地： y/n ")
    if n == 'n':
        i = False
    elif n == 'y':
        i = True
    else:
        print("输入错误")
        break
for name,value in mx.items():
    print(f"\n{name} 梦想去的地方是 {value}")