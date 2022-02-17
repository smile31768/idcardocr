from configparser import ConfigParser
import requests ,os, time
config = ConfigParser(allow_no_value=True)
#若不存在config配置，则新建一个
if not os.path.exists('config.conf'):
    config.add_section('ApplicationInfo')
    config['ApplicationInfo']={
        '# 在下方填写从百度申请的APP信息':None,
        'APIKey':'',
        'SecretKey':''
    }
    config.add_section('token')
    config['token']={
        '# 下方access_token自动生成，无需填写':None,
        'AccessToken':''
    }
    config.write(open('config.conf', 'w', encoding='UTF-8'), space_around_delimiters=False)
    print('config文件已生成，请打开填写AK和SK后重新打开本脚本获取access_token')
    time.sleep(2)
    quit()
config.read('config.conf', encoding='UTF-8')
#从config文件读取AK和SK
AK=config['ApplicationInfo']['APIKey']
SK=config['ApplicationInfo']['SecretKey']
if (AK=='')+(SK==''):
    print('未填写APIKey和SecretKey，请打开config.conf填写')
    time.sleep(2)
    quit()
#获取access_token
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+AK+'&client_secret='+SK
response = requests.get(host)
#提取access_token，并写入config
if response:
    Access_token=response.json()['access_token']
try:
    Access_token
except NameError:
    print('APIKey和SecretKey填写有误，access_token获取失败，请检查你的填写')
    time.sleep(2)
    quit()
config['token']={
    'AccessToken': Access_token
}
config.write(open('config.conf', 'w', encoding='UTF-8'), space_around_delimiters=False)