class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(self.name,self.type)

    def open_restaurant(self):
        print("餐馆正在营业")

    def set_number_served(self,number):
        self.number_served = number

    def incrember_number_served(self,number):
        self.number_served += number

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors =['巧克力','草莓','香草','芒果','酸奶']

    def show(self):
        for value in self.flavors:
            print (f"冰激凌的口味包括： {value}")

rest_0 = IceCreamStand('麦当劳','西餐厅')
rest_0.describe_restaurant()
rest_0.open_restaurant()
rest_0.set_number_served(45)
print(f"餐厅现在有{rest_0.number_served}人")
rest_0.show()
ic = input("请输入您要选择的口味： ")
if ic in rest_0.flavors:
    print(f"请稍等{ic}冰激凌马上帮您制作完成")
else:    
    print("抱歉输入错误，没有这个口味的冰激凌")
