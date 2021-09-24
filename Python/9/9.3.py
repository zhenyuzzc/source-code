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

zjf = User('朱','进峰','男','河北',16,'音乐')
zjf.describe_user()
zjf.greet_user()
print()

zzc = User('朱','震超','男','河北',40,'Python')
zzc.describe_user()
zzc.greet_user()
print()

hbh = User('胡','宝华','女','河北',40,'跳舞')
hbh.describe_user()
hbh.greet_user()
print()

hbh.increment_login_attempts()
print(hbh.login_attempts)
hbh.increment_login_attempts()
print(hbh.login_attempts)
hbh.increment_login_attempts()
print(hbh.login_attempts)
hbh.increment_login_attempts()
print(hbh.login_attempts)
hbh.increment_login_attempts()
print(hbh.login_attempts)
hbh.increment_login_attempts()
print(hbh.login_attempts)
hbh.reset_login_attemots()
print(hbh.login_attempts)
