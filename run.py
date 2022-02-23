import os,time
from bin.idocr import idocr
from bin.csvmod import create_csv,write_csv
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
if not os.path.exists('img'):
    os.mkdir('img')
    print('img文件夹不存在，已新建')
    time.sleep(2)
    quit()
if not os.listdir('img'):
    print('img文件夹无待识别图片')
    time.sleep(2)
    quit()
fail_count=0
csv_head=['姓名','民族','住址','身份证号','生日','性别']
create_csv(csv_head)            #创建csv文档
print('开始识别身份证')
for i in findAllFile('img'):    #遍历img文件夹，识别身份证信息
    idinfo=idocr(i)
    if not idinfo==[]:
        print(idinfo)
    else:
        fail_count+=1
    write_csv(idinfo)
    time.sleep(0.5)
print('正在写入xlsx文件')
csv2xlsx('output.csv','output.xlsx')
os.remove('output.csv')
print(f'识别完成，一共{fail_count}个识别失败')
time.sleep(2)
