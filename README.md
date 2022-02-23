# 基于百度AI的身份证图片批量OCR识别
使用百度大脑AI提供的API批量识别身份证信息，并制成Excel表格
## 使用方法
1. 首先，你需要有一个python3的环境
2. Clone本项目并cd进去
  ```bash
  git clone https://github.com/smile31768/idcardocr.git && cd ./idcardocr
  ```
3. 安装依赖[^1]
  ```bash
  pip install -i http://mirrors.aliyun.com/pypi/simple/ -r requirements.txt --trusted-host mirrors.aliyun.com
  ```
4. 运行get_token.py，会自动在目录下创建一个config.conf配置文件和img文件夹
5. 去[百度智能云](https://cloud.baidu.com/product/ocr_cards)官网的文字识别那里注册一个身份证识别[^2]
6. 领取后在官网控制台的应用列表里面创建一个应用，复制你的APIKey和SecretKey，填入config.conf文件里
  ```
  [ApplicationInfo]
  # 在下方填写从百度申请的app信息
  apikey=thisistheapikeyexample
  secretkey=thisisthesecretkeyexample

  [token]
  # 下方access_token自动生成，无需填写
  accesstoken=
  ```
7. 再次运行get_token.py，将会自动获取并写入access_token
8. 将你要识别的身份证图片放入img文件夹，运行run.py，运行完成后将会输出output.xlsx

[^1]:注意：依赖列表可能不完整，如果有缺少的依赖请自行安装
[^2]:百度一个月提供200次免费调用识别的额度可以领取
