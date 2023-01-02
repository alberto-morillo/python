
import requests
r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
print(f"status code: {r.status_code}")
# 200
print(f"content type: {r.headers['content-type']}")
# application/json; charset=utf8'
print(f"encoding type: {r.encoding}")
r.encoding
# 'utf-8'
print(f"it was successfully authenticated? {r.text}")
#{"authenticated": true, ...'
print(f"json response: {r.json()}")
#{'authenticated': True, ...}
