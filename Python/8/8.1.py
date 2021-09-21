def display_messgge():
    print("本章学习的函数")

display_messgge()

def favorite_book(tetle):
    print(f"我喜欢这本书{tetle.title()}")
favorite_book('python')

def make_shirt(xl,zi='I love you'):
    print(f"这件衣服的尺码是{xl},字样是{zi}")
make_shirt('大号')
make_shirt('中号','我就喜欢')

def describe_city(city,gj='中国'):
    print(f"{city}隶属于{gj}")
describe_city('北京')
describe_city('上海')
describe_city('东京','日本')