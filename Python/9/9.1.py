class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    
    def describe_restaurant(self):
        print(self.name,self.type)

    def open_restaurant(self):
        print("餐馆正在营业")

restaurant = Restaurant('华峰嘉业','中餐厅')
print(restaurant.name,restaurant.type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

rest_2 = Restaurant('烤鸭店','中餐厅')
rest_2.describe_restaurant()

rest_3 = Restaurant('比格','西餐厅')
rest_3.describe_restaurant()