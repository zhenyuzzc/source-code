names=[]
names.append('hubaohua')
names.append('zhujinfeng')
names.append('wanghuilan')
names.append('zhushuyin')
hi="欢迎你们能来一起共进晚餐"
print(f'hi {names[0]} {hi}')
print(f'hi {names[1]} {hi}')
print(f'hi {names[2]} {hi}')
print(f'hi {names[3]} {hi}')
names[2]='wanghuiping'
print(f'hi {names[0]} {hi}')
print(f'hi {names[1]} {hi}')
print(f'hi {names[2]} {hi}')
print(f'hi {names[3]} {hi}')
print('\n我找到了更大的餐桌')
names.insert(0,'liufulai')
names.insert(3,'wangliuchang')
names.append('chenyu')
print(f'hi {names[0]} {hi}')
print(f'hi {names[1]} {hi}')
print(f'hi {names[2]} {hi}')
print(f'hi {names[3]} {hi}')
print(f'hi {names[4]} {hi}')
print(f'hi {names[5]} {hi}')
print(f'hi {names[6]} {hi}')
print('\n餐桌订购失败只能邀请两名嘉宾')
yc=names.pop(0)
print(f'抱歉不能邀请您了 {yc}\n')
yc=names.pop(3)
print(f'抱歉不能邀请您了 {yc}\n')
yc=names.pop(2)
print(f'抱歉不能邀请您了 {yc}\n')
yc=names.pop(2)
print(f'抱歉不能邀请您了 {yc}\n')
yc=names.pop(2)
print(f'抱歉不能邀请您了 {yc}\n')
print(f'hi {names[0]} {hi}')
print(f'hi {names[1]} {hi}')
del names[0]
del names[0]
print(names)
names.append('hubaohua')
names.append('zhujinfeng')
names.append('wanghuilan')
names.append('zhushuyin')
print(names)
names.sort()
print(names)
names.sort(reverse=True)
print(names)
len(names)



