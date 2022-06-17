import pdfplumber
import xlwt
#import sys
#path = sys.argv[1]
#output = sys.ar1gv[2]
#print(sys.argv[1])
# 定义保存Excel的位置
workbook = xlwt.Workbook()  #定义workbook
sheet = workbook.add_sheet('Sheet1')  #添加sheet
i = 0 # Excel起始位置

#path = input("请输入PDF文件位置")
#path = 'E:/python/1.pdf‘
PATH = 'E:/python/1.pdf'
pdf = pdfplumber.open(PATH)
print('\n')
print('开始读取数据')
print('\n')
for page in pdf.pages:
    # 获取当前页面的全部文本信息，包括表格中的文字
    print(page.extract_text())
    for table in page.extract_tables():
        print(table)
        for row in table:
            print(row)
            for j in range(len(row)):
           # for j in enumerate(len(row)):
                sheet.write(i, j, row[j])
            i += 1
        print('---------- 分割线 ----------')

pdf.close()

# 保存Excel表
workbook.save('E:/python/PDFresult.xls')
print('\n')
print('写入excel成功')
print('保存位置：')
print('E:/python/PDFresult.xls')
print('\n')
input('PDF取读完毕，按任意键退出')
