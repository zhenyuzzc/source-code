favorite_places = {
    'zhuzhenchao': {
        'firt':'beijing',
        'last':'xitan',
        'ds':'shanghai',
        },
    'zhujinfeng':{
        'firt':'xian',
        'last':'tianjin'
        },
    'hubaohua':
        {'firt':
        'longhua',
        }
    }
for names,value in favorite_places.items():
    print(names.title(),"喜欢的城市")
    for dm in value.values():
        print("\t",dm)
    print()