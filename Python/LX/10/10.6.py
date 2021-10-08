while True:
    try:
        num_1 = input("输入第一个数:  ")
        num_2 = input("输入第二个数:  ")
        sum = int(num_1)+int(num_2)
        print(sum)
    except ValueError:
        pass
