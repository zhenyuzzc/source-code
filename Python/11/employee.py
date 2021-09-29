class Employee:
    """定义Employee类并附属性"""
    def __init__(self,xing,ming,nianxin=0):
        self.xing = xing 
        self.ming = ming
        self.nianxin = nianxin

    def give_raise(self,nianxin_plus=5000):
        """方法give_raise使年薪加5000"""
        self.nianxin += nianxin_plus
        return (self.nianxin)

    
