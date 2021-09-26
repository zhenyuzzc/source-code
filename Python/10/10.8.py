def read(filename):
    try:
        with open(filename,encoding='utf-8') as f:
            file = f.read()
    except FileNotFoundError:
        pass  
    else:   
        num = file.lower().count(' the ')
        print(num)

list = ['cats.txt','dogs.txt','alice.txt']   
for value in list:
    read(value)

