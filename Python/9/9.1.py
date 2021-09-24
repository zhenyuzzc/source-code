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

rest_1 = Restaurant('华峰嘉业','中餐厅')
print(rest_1.name,rest_1.type)

rest_1.describe_restaurant()
rest_1.open_restaurant()

rest_2 = Restaurant('烤鸭店','中餐厅')
rest_2.describe_restaurant()

rest_3 = Restaurant('比格','西餐厅')
rest_3.describe_restaurant()
print(f"有{rest_3.number_served}人在这家餐馆就餐")
rest_3.set_number_served(100)
print(f"这家餐馆现有{rest_3.number_served}")
rest_3.incrember_number_served(150)
print(f"这家餐馆最多能容纳{rest_3.number_served}")