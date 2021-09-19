cities = {
    'beijing':{
        'country':'china',
        'populatino':'50000000',
        'fact':'四季分明',
    },
    'shanghai':{
        'country':'china',
        'populatino':'30000000',
        'fact':'潮湿',
    },
    'hangzhou':{
        'country':'china',
        'populatino':'40000000',
        'fact':'湿热',
    }
}
cities['hainan']={
        'country':'china',
        'populatino':'200000',
        'fact':'水果',}
for name,value in cities.items():
    print(f"所在城市{name.title()}")
    for k,v in value.items():
        print("\t",k,v)
print()
for name,value in cities.items():
    print(f"所在城市{name.title()}")
    print(f"\tcountry：{value['country']} / populatino：{value['populatino']} / fact：{value['fact']}\n")

value = cities.get('tainjing','不存在')
print(value)