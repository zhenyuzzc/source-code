names_0 = {'last_name':'jinfeng','firt_name':'zhu','age':'16','city':'beijing'}
names_1 = {'last_name':'zhenchao','firt_name':'zhu','age':'40','city':'beijing'}
names_2 = {'last_name':'baohua','firt_name':'hu','age':'40','city':'beijing'}
people = [names_0,names_1,names_2]
for value in people:
    full_name = f"{value['firt_name']}{value['last_name']}"
    print(f"姓名：{full_name.title()} 年龄：{value['age']} 所在地： {value['city'].title() }\n")
    