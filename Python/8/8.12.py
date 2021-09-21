def smz(*cailiao):
    print("\n原材料包括：")
    for value in cailiao:
        print(f"-{value}")

smz('牛肉')
smz('牛肉','西红柿')
smz('牛肉','土豆','西红柿','芝士')
