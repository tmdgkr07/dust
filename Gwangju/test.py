
#-*-coding:utf-8-*-
import requests
import urllib.request
import pandas as pd
import json
import pprint

dust_data=' '

api_key = "1FmuBg8TmJiwfSk8v7kigut57VG5pwtbsovBmJDPqCHLQm%2Bbd3uZi9k1hXIswLNsSnXxNnAH7ysAEkev4z1%2BHw%3D%3D"

dust = 'dust'

city = "광주"

dust_File = 'dust_Gwangju.json'

url_dust = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=" + city + "&searchCondition=HOUR&pageNo=1&numOfRows=100&ServiceKey=" + api_key + "&ver=1.3&_returnType=json"

def dust(request):

        #api 에서 호출된 값중 원하는 값만 불러오기

    pm10 = request['pm10Value']
    print(pm10)

def request_dust():

        #api 호출 및 데이터 값을 json으로 정렬

    request = urllib.request.Request(url_dust)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if(rescode==200):
        response_body=response.read()
       # print(response_body.decode('utf-8'))
        dict = json.loads(response_body.decode('utf-8'))

        try:
            if dust:
                i = 0
                pm_data = dict['list'][i]
                
            else:
                pass

            if dust:
                dust(pm_data)
            else:
                pass
        except:
            pass

        
    else:
        print(rescode)
    with open( dust_File ,'w', encoding="utf-8") as make_file:
        json.dump(dict, make_file, ensure_ascii=False, indent="\t")

if __name__=='__main__':
     
    request_dust()
