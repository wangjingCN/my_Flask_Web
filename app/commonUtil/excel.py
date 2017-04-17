#!/usr/bin/env python
# -*- coding: utf-8 -*-
from xlrd import open_workbook, xldate
from xlutils.copy import copy
import xlwt


def edit_excel(filename, base_id=[]):
    font0 = xlwt.Font()
    font0.name = 'Times New Roman'
    font0.colour_index = 2  # 红色
    font0.bold = True

    style0 = xlwt.XFStyle()
    style0.font = font0

    style1 = xlwt.XFStyle()
    style1.num_format_str = 'YYYY/MM/DD'  # 对日期格式的处理

    rb = open_workbook(filename)
    # rb_cols_len = rb.sheet_by_index(0).ncols  # 原表的列数
    wb = copy(rb)
    ws = wb.get_sheet(0)
    table = rb.sheets()[0]
    for row_number in range(table.nrows):
        if row_number == 0:
            ws.write(0, 2, u"是否包含", style0)  # 新增一列

        else:
            if table.row_values(row_number)[0] in base_id:
                ws.write(row_number, 0, table.row_values(row_number)[0], style0)  # 这个地方需要改一个颜色
                ws.write(row_number, 2, u'是', style0)  # 给新增的列添加内容
            else:
                ws.write(row_number, 2, u'否')  # 给新增的列添加内容
                # ws.write(row_number, 1, xldate.xldate_as_datetime(table.row_values(row_number)[1], 0), style1)  # 这个地方需要写成日期格式

    # wb.save(filename)#覆盖原文件
    wb.save('new_' + filename)  # 可以把文件保存为另外的名字，原文件不会改变
    print 'ok'


def get_excel_base_ids(base_filename):
    data = open_workbook(base_filename)  # 打开xls文件
    base_id = []
    table = data.sheets()[0]  # 打开第一张表
    for i in range(table.nrows):  # 按行循环
        if i:  # 跳过第一行
            try:
                base_id.append(table.row_values(i)[1])  # 读第二列
            except Exception:
                base_id.append(table.row_values(i)[0])  # 读第一列

    return base_id


# print len(get_excel_base_ids(u'10Y.xlsx'))
# print edit_excel(u'10s.xlsx', get_excel_base_ids(u'10Y.xlsx'))
print edit_excel('aa.xlsx', get_excel_base_ids('a.xlsx'))
# print get_excel_base_ids(u'a.xlsx')
