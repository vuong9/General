import urllib.parse
import urllib.request

url = 'http://google.com'
'''
info = {'user':'admin','passwd':'admin'}
data = urllib.parse.urlencode(info).encode()
req = urllib.request.Request(url,data)
with urllib.request.urlopen(req) as response:
    content = response.read()'''
with urllib.request.urlopen(url) as response:
    content =response.read()

print(content)