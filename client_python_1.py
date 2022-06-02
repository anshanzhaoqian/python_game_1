import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest'
}

a = input('ip:')
url = "http://192.168.60." + a + ":5000/signUpUser"

s = requests.Session()

a = input('shitou, jianzi, bu, q:')
while a != 'q':
  myobj = {"key": a}
  content = s.post(url, data=myobj, headers=headers)
  print(content.text)
  a = input('shitou, jianzi, bu, q:')
  












