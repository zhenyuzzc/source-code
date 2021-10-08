import xlrd
import xlwt
from xlutils.copy import copy
#from datetime import datetime,date

row = [] #存储每行数据的空列表
data = xlrd.open_workbook('订单信息.xlsx') #打开工作表
sheet_name = data.sheet_names() #获取所有工作表的名字
sheet1 = data.sheet_by_name('厨房支架') #用工作表名获取其内容并赋值给表量
row_number = sheet1.nrows #获取工作表的总行数

#遍历工作表每行内容并赋值到row列表
for value in range(1,row_number):
    row.append(sheet1.row_values(value))
#for index,value in enumerate(row[0]): 查询每行数据对应的索引值

def my_style_1():
    """设置字体、边框、居中样式"""
    
    font = xlwt.Font() #设置字体样式
    font.name = '微软雅黑'
    font.bold = True
    font.height = 240
    
    borders =xlwt.Borders() #设置边框样式
    borders.bottom = xlwt.Borders.THIN
    
    alignment = xlwt.Alignment() #设置单元格位置
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    
    my_style = xlwt.XFStyle() #初始化样式
    my_style.font = font
    my_style.borders = borders
    my_style.alignment = alignment
    
    return my_style


readbook = xlrd.open_workbook('送货通知书/杭州送货通知书.xls',formatting_info=True) #复制工作表用来添加数据
wb = copy(readbook)
ws = wb.get_sheet(0)

dh_date = input('输入到货日期（格式2021-01-01）： ') #输入到货日期赋值到变量dh_date

for value in range(len(row)):
    style_1 = my_style_1()
    ws.write(3,1,row[value][7],style_1) #写入公司信息
    ws.write(10,3,dh_date,style_1) #写入到货日期
    ws.write(12,3,row[value][3],style_1) #写入订单号
    ws.write(18,3,row[value][22],style_1) #写入品相名称
    ws.write(20,3,row[value][21],style_1) #写入品相JDE
    ws.write(22,3,row[value][14],style_1) #写入收货数量
    ws.insert_bitmap('送货通知书/hz_logo.bmp',0,4) #插入图片
    wb.save(f'送货通知书/hangzhou_new/{row[value][3]}杭州送货通知书.xls') #保存工作簿
