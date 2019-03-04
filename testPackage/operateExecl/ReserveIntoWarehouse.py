# -*- coding: utf-8 -*-

import xlrd
import pymysql
import sys
# Open the workbook and define the worksheet
book = xlrd.open_workbook("倒车入库-version-1(实际值).xlsx", logfile=sys.stdout)
sheet = book.sheet_by_name("0308所有接口QPS")

# 建立一个MySQL连接
connection = pymysql.connect (host="127.0.0.1", port=6006, user = "root", passwd = "123456", db = "test",)

# 获得游标对象, 用于逐行遍历数据库数据
cursor = connection.cursor()

# 创建插入SQL语句
query = """INSERT INTO save (instance_name, exp_190311, exp_190311_single, max181111, max180919, max180515, max180311, max171111, max170923, max170515, max170311) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

# 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题
for r in range(2, sheet.nrows):
      instance_name = sheet.cell(r,1).value.strip()
      max181111 = sheet.cell(r,2).value if sheet.cell(r,2).value else "0"
      max180919 = sheet.cell(r,3).value if sheet.cell(r,3).value else "0"
      max180515 = sheet.cell(r,4).value if sheet.cell(r,4).value else "0"
      max180311 = sheet.cell(r,5).value if sheet.cell(r,5).value else "0"
      max171111 = sheet.cell(r,6).value if sheet.cell(r,6).value else "0"
      max170923 = sheet.cell(r,7).value if sheet.cell(r,7).value else "0"
      max170515 = sheet.cell(r,8).value if sheet.cell(r,8).value else "0"
      max170311 = sheet.cell(r,9).value if sheet.cell(r,9).value else "0"
      exp_190311  = sheet.cell(r,10).value if sheet.cell(r,10).value else "0"
      exp_190311_single = sheet.cell(r,14).value if sheet.cell(r,14).value else "0"
      print(instance_name,max181111,max180919,max180515,max180311,max171111,max170923,max170515,max170311,exp_190311 ,exp_190311_single)
      values = (instance_name, exp_190311, exp_190311_single, max181111,max180919,max180515,max180311,max171111,max170923,max170515,max170311)
      # 执行sql语句
      cursor.execute(query, values)

# 关闭游标
cursor.close()
# 提交
connection.commit()
# 关闭数据库连接
connection.close()
