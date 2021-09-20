while True:
    age = input("请输入你的年龄： ")
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("您的年龄小于3岁，票价免费。")
        elif age < 12:
            print("您的年龄小于12岁，票价10美元。")
        else:
            print("您的年龄大于12岁，票价15美元。")