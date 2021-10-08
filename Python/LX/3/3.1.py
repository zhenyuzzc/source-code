names=['zhenchaozhu','chenyanfeng','wangyuping','liulei']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
hello="你好，欢迎光临"
print(f'{names[0]} {hello}')
print(f'{names[1]} {hello}')
print(f'{names[2]} {hello}')
print(f'{names[3]} {hello}')
names[0]='zhuzhenchao'
names.append('zhujinfeng')
print(names)
names.insert(1,'hubaohua')
print(names)
del names[2]
print(names)
gs=names.pop(2)
print(names)
print(gs)
names.remove('liulei')
print(names)
