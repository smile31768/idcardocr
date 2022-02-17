import os,time
from bin.idocr import idocr
from bin.csvmod import create_csv,write_csv
from bin.convert import csv2xlsx
import pandas as pd
# 遍历目录文件
def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname
# csv转xlsx
def csv2xlsx(csvpath,xlsxpath):
    csv = pd.read_csv(csvpath, encoding='utf-8',dtype=object)
    csv.to_excel(xlsxpath, sheet_name='sheet1',index=False)

# main
csv_head=['姓名','民族','住址','身份证号','生日','性别']
create_csv(csv_head)            #创建csv文档
for i in findAllFile('img'):    #遍历img文件夹，识别身份证信息
    idinfo=idocr(i)
    print(idinfo)
    write_csv(idinfo)
    time.sleep(0.5)
print('正在写入xlsx文件')
csv2xlsx('output.csv','output.xlsx')
os.remove('output.csv')