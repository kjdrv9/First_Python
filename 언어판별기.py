import os
import sys
import urllib.request
import json
dic = {'ko': '한국어', 'ja': '일본어', 'zh-cn': '중국어간체', 'zh-tw': '중국어번체', 'hi': '힌디어', 'en': '영어', 'es': '스페인어', 'fr': '프랑스어', 'de': '독일어', 'pt': '포르투갈어', 'unk': '알수없음'}
client_id = "iKi1ibEO4Rli14GeR6_C"
client_secret = "GbqUqFKGSq"
encQuery = urllib.parse.quote(input())
data = "query=" + encQuery
url = "https://openapi.naver.com/v1/papago/detectLangs"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    result = json.loads(response_body.decode("utf-8"))
    lang = result["langCode"]
    lang = lang.lower()
    try:
        print(dic[lang])
    except KeyError:
        print("이 언어는 지원되지 않습니다.")
else:
    print("Error Code:" + rescode)
