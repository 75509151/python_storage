import urllib2

try:
    response = urllib2.urlopen("http://blog.csdn.net/pleasecallmewhy/article/details/8923067")
    print response.read()
except urllib2.HTTPError, e:
    print e
    print e.code
    print e.reason
except urllib2.URLError, e:
    print e

print "\033[1;31m over \033[0m"

# we can see, the response does not  return what we need
# http exception
import urllib

url = "http://blog.csdn.net/pleasecallmewhy/article/details/8923067"
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
headers = {'User-Agent': user_agent, 'Referer': 'http: // blog.csdn.net /'}
# data = urllib.urlencode()
request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)
page = response.read()
print page

# we can set http headers, use user_agent ,
# request: url , data, headers


import urllib2
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http": 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

# proxy


httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
# response = urllib2.urlopen('http://www.baidu.com')
response = opener.open(urllib2.Request("http://www.baidu.com"))
# debuglog and opener
