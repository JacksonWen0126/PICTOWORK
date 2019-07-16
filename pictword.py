# coding:utf-8
import base64,urllib.parse,urllib.request,urllib.error


access_token = '24.14d4cf2e93345ddfe663236f90aaddb1.2592000.1565819100.282335-16814012'
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=' + access_token

f = open(r'pic1.png', 'rb')
# encode picture to base64
img = base64.b64encode(f.read())
params = {"image": img}
params = urllib.parse.urlencode(params)
data = params.encode('utf-8')
r = urllib.request.Request(url,data=data)
r.add_header('Content-Type', 'application/x-www-form-urlencoded')
r = urllib.request.urlopen(r)
content = r.read().decode()
if(content):
    print(content)