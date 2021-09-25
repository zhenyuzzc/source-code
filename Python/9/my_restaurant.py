class User:
    def __init__(self,first_name,last_name,xb,jg,age,love):
        self.first_name = first_name
        self.last_name = last_name
        self.xb = xb
        self.jg = jg
        self.age = age
        self.love = love
        self.login_attempts = 0

    def describe_user(self):
        print(f"姓名：{self.first_name}{self.last_name}")
        print(f"个人信息：\n性别：{self.xb}\n籍贯：{self.jg}\n年龄：{self.age}\n喜好：{self.love}")

    def greet_user(self):
        print(f"{self.first_name}{self.last_name} 欢迎你的加入")

    def increment_login_attempts(self):
        self.login_attempts =self.login_attempts + 1

    def reset_login_attemots(self):
        self.login_attempts = 0

