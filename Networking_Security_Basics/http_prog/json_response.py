import urllib.request
import json

url = 'http://httpbin.org/get'
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode('utf-8'))
    print(data)