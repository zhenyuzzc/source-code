def city_country(city,gj):
    full_name = f"{city},{gj}"
    print(full_name)

city_country('北京','中国')
city_country('上海','中国')
city_country('东京','日本')

def make_album(name,zj):
    zd = {'姓名':name,'专辑':zj}
    return zd
value = make_album('朱进峰','我的最爱')
print(value)

def make_album(name,zj,sl=None):
    zd = {'姓名':name,'专辑':zj}
    if sl:
        zd['数量'] = sl
    return zd

dict_0 = make_album('朱进峰','我的最爱')
print(dict_0)
dict_1 = make_album('朱进峰','太多',sl=10)
print(dict_1)
dict_2 = make_album('朱进峰','一个人')
print(dict_2)