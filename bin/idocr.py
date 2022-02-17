# encoding:utf-8
import requests,base64,os,time
from configparser import ConfigParser
def idocr(filepath):        # 身份证OCR识别函数，参数为识别图片二进制文件路径
    # 读取access_token
    config = ConfigParser()
    if not os.path.exists('config.conf'):
        print('config文件不存在，请运行get_token生成')
        time.sleep(2)
        quit()
    config.read('config.conf', encoding='UTF-8')
    access_token=config['token']['accesstoken']
    if (access_token is None)+(access_token==''):
        print('accesstoken未获取，请通过get_token获取')
        time.sleep(2)
        quit()
    # 百度大脑AI接口识别身份证信息
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard"
    # 二进制方式打开图片文件
    f = open(filepath, 'rb')
    img = base64.b64encode(f.read())
    params = {"id_card_side":"front","image":img}
#   access_token = ''
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        idinfo=response.json()
    # 提取有用信息
    if 'words_result' in idinfo:
        birthday=list(idinfo['words_result']['出生']['words'])
        birthday.insert(4,'/')
        birthday.insert(7,'/')
        birthday=''.join(birthday)
        idresult=[idinfo['words_result']['姓名']['words'],idinfo['words_result']['民族']['words'],idinfo['words_result']['住址']['words'],idinfo['words_result']['公民身份号码']['words'],birthday,idinfo['words_result']['性别']['words']]
    else:
        idresult=['No recognized data.']
    return (idresult)
