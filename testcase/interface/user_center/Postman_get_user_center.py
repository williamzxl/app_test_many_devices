import requests

url = "https://appncee.langlib.com/userStudyCenter/serviceInfo"

querystring = {"serviceID":""}

headers = {
    'platform': "Android",
    'appkey': "CEE_AA8F55B916AB",
    'appversion': "10000005",
    'appsecret': "3DB5159C-EB1E-47FE-8584-47115EF5E443",
    'app': "cee",
    'accesstoken': "828007cd-7234-4440-aebb-02ef5a08f4cc",
    'host': "appncee.langlib.com",
    'connection': "Keep-Alive",
    'accept-encoding': "gzip",
    'user-agent': "okhttp/3.11.0",
    'cache-control': "no-cache",
    'postman-token': "5c07a19c-9adb-b1e3-0184-e1ed3cfcab83"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)