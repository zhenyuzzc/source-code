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
for name,value in cities.items():
    print(name.title())
    for k,v in value.items():
        print("\t",k,v)