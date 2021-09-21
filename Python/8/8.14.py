def cars(pb,cx,**cs):
    cs['品牌'] = pb
    cs['车型'] = cx
    return cs

car = cars('斯巴鲁','傲虎',
            颜色='珍珠白',
            驾驶辅助系统='视驭')
print(car)