class Employee:
    """定义Employee类并附属性"""
    def __init__(self,xing,ming,nianxin):
        self.xing = xing 
        self.ming = ming
        self.nianxin = nianxin

    def give_raise(self):
        """方法give_raise使年薪加5000"""
        self.nianxin += 5000
        return self.nianxin
