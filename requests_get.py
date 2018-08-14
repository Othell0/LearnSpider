import requests
import webbrowser

param = {'wd': '虎牙'}
r = requests.get('http://www.baidu.com/s', param)
print(r.url)
webbrowser.open(r.url)
