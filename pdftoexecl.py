# -*- coding: utf-8 -*-
import pdfplumber


import xlwt

workbook = xlwt.Workbook()

sheet = workbook.add_sheet('Sheet1')

i = 0
#path = input("请输入PDF文件位置：")    
path = "D:/Dowmload/1.PDF"  
pdf = pdfplumber.open(path)

print('开始读取数据')

for page in pdf.pages:

  for table in page.extract_tables():

     for row in table: 
         print(row)

         for j in range(len(row)):

             sheet.write(i, j, row[j])

         i += 1
         print('---------- 分割线 ----------')

pdf.close()

workbook.save('C:/Users/Administrator/Desktop/result.xls')

print('保存成功！')
import pdfplumber
import xlwt

workbook = xlwt.Workbook()

sheet = workbook.add_sheet('Sheet2')

i = 0

pdf = pdfplumber.open(path)

print('开始读取数据')

for page in pdf.pages:

   for table in page.extract_tables():

       for row in table:

             for j in range(len(row)):

                  sheet.write(i, j, row[j])

             i += 1

pdf.close()

workbook.save('C:/Users/Administrator/Desktop/result.xls')

print('保存成功！')