import json

def read():
    """读取数据函数"""
    file_path = 'e:/zzc/numbers.json'
    try:
        with open(file_path) as f:
            file = json.load(f)
    except FileNotFoundError:
        pass
    else:
        return file

def writ():
    """写入数据函数"""
    num = input("输入一个数： ")
    file_path = 'e:/zzc/numbers.json'
    with open(file_path,'w') as f:
        file = json.dump(int(num),f)
    return file

def number():
    """调用前面两个函数"""
    file = read()
    if file:
       print(f"这是你喜欢的数字 {file}")
    else:
        file = writ()
        file = read()
        print(f"这是你喜欢的数字 {file}")

number()
i = input("要重新输入吗 y/n：")
if i == 'y':
    file = writ()
    file = read()
    print(f"这是你喜欢的新数字 {file}")
elif i == 'n':
    print("已退出")
else:
    print("输入错误")