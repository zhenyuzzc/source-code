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
    font.bold = True #字体加粗
    font.height = 240 #字号由20*12得来即12号字体
    
    borders =xlwt.Borders() #设置边框样式
    borders.bottom = xlwt.Borders.THIN #下边框
    
    alignment = xlwt.Alignment() #设置单元格位置
    alignment.horz = xlwt.Alignment.HORZ_CENTER #水平居中
    alignment.vert = xlwt.Alignment.VERT_CENTER #垂直居中
    
    my_style = xlwt.XFStyle() #初始化样式
    my_style.font = font
    my_style.borders = borders
    my_style.alignment = alignment
    
    return my_style

def my_style_2():
    """设置字体、边框、居中样式"""
    
    font = xlwt.Font() #设置字体样式
    font.name = '微软雅黑'
    font.bold = False
    font.height = 240
    
    borders =xlwt.Borders() #设置边框样式
    borders.bottom = xlwt.Borders.THIN
    
    alignment = xlwt.Alignment() #设置单元格位置
    alignment.horz = xlwt.Alignment.HORZ_LEFT
    alignment.vert = xlwt.Alignment.VERT_CENTER
    
    my_style = xlwt.XFStyle() #初始化样式
    my_style.font = font
    my_style.borders = borders
    my_style.alignment = alignment
    
    return my_style

merged = sheet1.merged_cells #获取表格中所有合并单元格位置，以列表形式返回（起始行，结束行，起始列，结束列）
#print(merged)
def get_cell_type(row_index, col_index):
    """既能得到合并单元格也能得到普通单元格"""
    cell_value = None
    for (rlow, rhigh, clow, chigh) in merged:  # 遍历表格中所有合并单元格位置信息
        # print(rlow,rhigh,clow,chigh)
        if (row_index >= rlow and row_index < rhigh):  # 行坐标判断
            if (col_index >= clow and col_index < chigh):  # 列坐标判断
                #如果满足条件，就把合并单元格第一个位置的值赋给其它合并单元格
                cell_value = sheet1.cell_value(rlow, clow)
                #print('合并单元格')
                break  # 不符合条件跳出循环，防止覆盖
            else:
                #print('普通单元格')
                cell_value = sheet1.cell_value(row_index, col_index)
 
        else:  #添加改行后的那一个单元格的内容5，0 会返回2个值普通单元格/合并单元格
            #print('普通单元格')
            cell_value = sheet1.cell_value(row_index, col_index)
 
    return cell_value


readbook = xlrd.open_workbook('送货通知书/杭州送货通知书.xls',formatting_info=True) #复制工作表用来添加数据
wb = copy(readbook)
ws = wb.get_sheet(0)

dh_date = input('输入到货日期（格式2021-01-01或2021/01/01）： ') #输入到货日期赋值到变量dh_date

i = 1
for value in row:
    style_1 = my_style_1()
    style_2 = my_style_2()
    ws.write(3,1,get_cell_type(i,7),style_2) #写入公司信息
    ws.write(10,3,dh_date,style_1) #写入到货日期
    ws.write(12,3,get_cell_type(i,3),style_1) #写入订单号
    ws.write(18,3,value[22],style_1) #写入品相名称
    ws.write(20,3,value[21],style_1) #写入品相JDE
    ws.write(22,3,value[14],style_1) #写入收货数量
    ws.insert_bitmap('送货通知书/hz_logo.bmp',0,4) #插入图片
    wb.save(f'送货通知书/hangzhou_new/{get_cell_type(i,3)}-{int(value[21])}杭州送货通知书.xls') #保存工作簿
    i += 1
