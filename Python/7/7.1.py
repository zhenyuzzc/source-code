car= input("请问要租赁什么样的汽车:" )
print(f"Let me see if I can find you a {car.title()}")

user = input("请问一共几位客人：" )
user = int(user)
if user > 8:
    print("不好意思已经没8位以上的桌子")
else:
    print("好的，请跟我这里走")

sz = input("请输入一共数:" )
sz = int(sz)
if sz%10 == 0:
    print(f"该数{sz}是10的整数倍")
else:
    print(f"这个数{sz}不是10的整数倍")

