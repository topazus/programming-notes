import json
import urllib3
import urllib.request

http=urllib3.PoolManager()
r=http.request('GET','https://api.github.com/repos/v2ray/v2ray-core/releases/latest')
data=json.loads(r.data.decode('utf-8'))


with urllib.request.urlopen('https://api.github.com/repos/v2ray/v2ray-core/releases/latest') as f:
    data=json.loads(f.read())
    tag_name=data['tag_name'][1:]

