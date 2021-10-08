user = {
    'username':'efermi',
    'first':'eaerico',
    'last':'fermi',
}
dc = ['username','first']
for name in user.keys():
    if name in dc:
        print(f"感谢{name.title()}参加调查")
    else:
        print(f"邀请{name.title()}来参加调查")