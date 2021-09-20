pizz = []
i = True
while i:
    pl = input("请输入配料名：")
    if pl != 'quit':
        print(f"我们会在披萨中添加这种配料{pl}")
        pizz.append(pl)
    else:
        i = False
print(f"备料包括{pizz}")