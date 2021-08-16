import urllib.request
from urllib.request import Request

url = 'http://python.org'
user_agent = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile ' \
             'Safari/537.36 '


def chrome_user_agent():
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', user_agent)]
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(url)
    print('Response headers')
    print('----------------')
    for header, value in response.getheaders():
        print(header + ':' + value)

    request = Request(url)
    request.add_header('User-agent', user_agent)
    print('\nRequest headers')
    print('--------------------')
    for header, value in request.header_items():
        print(header + ':' + value)


if __name__ == '__main__':
    chrome_user_agent()
