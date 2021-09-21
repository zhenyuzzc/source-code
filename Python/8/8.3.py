
def make_album(name,zj,sl=None):
    zd = {'姓名':name,'专辑':zj}
    if sl:
        zd['数量'] = sl
    return zd
while True:
    print("请输入歌手和专辑名")
    print("退出请输入 q ")
    name = input("姓名： ")
    if name == "q":
        break
    zj = input("专辑名： ")
    if zj == "q":
        break
    i = make_album(name,zj)
    print(i)
