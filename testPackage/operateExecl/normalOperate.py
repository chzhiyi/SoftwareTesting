# -*- coding: utf-8 -*-

import xlrd
import sys

book = xlrd.open_workbook("倒车入库-version-1(实际值).xlsx", logfile=sys.stdout)
sheet = book.sheet_by_name("0308所有接口QPS")


# 获取各行名
def get_rows_name(var_sheet):
    for i in range(var_sheet.nrows):
        print(var_sheet.cell(i, 2), var_sheet.cell_type(i, 2), var_sheet.cell_value(i, 2))


# 获取各列名
def get_cols_name(var_sheet):
    for i in range(var_sheet.ncols):
        print(var_sheet.cell(0, i), var_sheet.cell_type(0, i), var_sheet.cell_value(0, i))


# 两个方法获取sheet名称
def two_methods_get_sheet_names(var_book):
    # one
    print(var_book.sheet_names())
    # two
    for i in range(var_book.nsheets):
        print(var_book.sheet_by_index(i).name, type(var_book.sheet_by_index(i)))


# 获取列名跟index的对应关系
def get_name_index_relationship(var_sheet):
    var_col_names = {}
    for i in range(var_sheet.ncols):
        var_col_names[var_sheet.cell_value(0, i)] = i
    return var_col_names


# 打印列名跟index的对应关系
def print_name_index_relationship(var_dict):
    for k, v in var_dict.items():
        print(k,v)


# 根据列名获取列索引
def get_columnIndex(var_dict, column_name):
    return var_dict[column_name] if var_dict[column_name] else -1


def main():
    # two_methods_get_sheet_names(book)
    # get_cols_name(sheet)
    # get_rows_name(sheet)
    col_name_dist = get_name_index_relationship(sheet)
    print_name_index_relationship(col_name_dist)

    col_name = "20180919"
    print('------我是分割线------')
    for i in 1,2,3:
        print(sheet.cell_value(i, col_name_dist[col_name]))


if __name__ == '__main__':
    main()
