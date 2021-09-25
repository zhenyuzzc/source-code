from my_restaurant import User
class Privileges:
    def __init__(self,privileges = ['can add post',
                                    'can delete post',
                                    'can ban user'
                                    ]):
        self.privileges = privileges
    
    def show_privileges(self):
        for value in self.privileges:
            print(value)

class Admin(User):
    def __init__(self,first_name,last_name,xb,jg,age,love):
        super().__init__(first_name,last_name,xb,jg,age,love)
        self.xl = Privileges()