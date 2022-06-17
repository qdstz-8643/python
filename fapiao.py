"-*- coding: utf-8 -*-"
import pdfplumber
import re
import os


def re_text(bt, text):
    m1 = re.search(bt, text)
    if m1 is not None:
        return re_block(m1[0])


def re_block(text):
    return text.replace(' ', '').replace('　', '').replace('）', '').replace(')', '').replace('：', ':')


def get_pdf(dir_path):
    pdf_file = []
    for root, sub_dirs, file_names in os.walk(dir_path):
        for name in file_names:
            if name.endswith('.pdf'):
                filepath = os.path.join(root, name)
                pdf_file.append(filepath)
    return pdf_file


def read():
    filenames = get_pdf('C:/Users/Administrator/Desktop/a')  # 修改为自己的文件目录
    for filename in filenames:
        print(filename)
        with pdfplumber.open(filename) as pdf:
            first_page = pdf.pages[0]
            pdf_text = first_page.extract_text()
            if '发票' not in pdf_text:
                continue
            # print(pdf_text)
            print('--------------------------------------------------------')
            print(re_text(re.compile(r'[\u4e00-\u9fa5]+电子普通发票.*?'), pdf_text))
            t2 = re_text(re.compile(r'[\u4e00-\u9fa5]+专用发票.*?'), pdf_text)
            if t2:
                print(t2)
            # print(re_text(re.compile(r'发票代码(.*\d+)'), pdf_text))
            print(re_text(re.compile(r'发票号码(.*\d+)'), pdf_text))
            print(re_text(re.compile(r'开票日期(.*)'), pdf_text))
            print(re_text(re.compile(r'名\s*称\s*[:：]\s*([\u4e00-\u9fa5]+)'), pdf_text))
            print(re_text(re.compile(r'纳税人识别号\s*[:：]\s*([a-zA-Z0-9]+)'), pdf_text))
            price = re_text(re.compile(r'小写.*(.*[0-9.]+)'), pdf_text)

            print(price)
            company = re.findall(re.compile(r'名.*称\s*[:：]\s*([\u4e00-\u9fa5]+)'), pdf_text)
            if company:
                print(re_block(company[len(company)-1]))
            print('--------------------------------------------------------')


read()
import xlwt

# 创建工作簿
wb = xlwt.Workbook()
# 创建表单
sh = wb.add_sheet('sheet 1')
# 写入数据
sh.write(0, 1, '姓名')
# 保存
wb.save('test.xls')

from gooey import Gooey, GooeyParser


@Gooey(program_name="简单的实例")
def main():
    parser = GooeyParser(description="第一个示例!")
    parser.add_argument('文件路径', widget="FileChooser")  # 文件选择框
    parser.add_argument('日期', widget="DateChooser")  # 日期选择框
    args = parser.parse_args()  # 接收界面传递的参数
    print(args)


if __name__ == '__main__':
    main()
