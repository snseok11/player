from urllib.parse import urlencode, unquote, quote_plus
import requests
from bs4 import BeautifulSoup
from time import time, localtime
#from .models import checkair_1
#from .models import checkair_2


#def real_time (request) :
 #   a = time()
  #  localtime_kr = localtime(a)
   # if localtime_kr.tm_min == '1' :
    #    checkair_1.objects.all().delete()
     #   model_input_dict = check_air_1(request)
      #  for i,j in model_input_dict :
       #     checkair_1(station=i , pm10=j).save
    #else :
     #   return None
    

#def real_time_2(request) :
    #a = time()
    #localtime_kr = localtime(a)
    #if localtime_kr.tm_min == '1' :
     #   checkair_2.objects.all().delete()
      #  model_input_dict = check_air_2(request)
       # for i,j in model_input_dict :
        #    checkair_2(data_time=i , pm10=j).save
    #else : 
     #   return None

serviceKey = "0eC9FQ3sjJfOFgDhUwnwj%2BtT2FBCBEKAJQV1RwtgxJxTEplfXC%2FuV7L%2BXIi2b5SnYsfikgaWL08KHczUyqqfjQ%3D%3D"
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')

def check_air_1(request):
    station = []
    pm10 = []
    url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
    returnType="xml"
    numOfRows="100"
    pageNo="1"
    sidoName=request
    ver="1.0"

    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : serviceKeyDecoded, quote_plus('returnType') : returnType, quote_plus('numOfRows') : numOfRows, quote_plus('pageNo') : pageNo, quote_plus('sidoName') : sidoName, quote_plus('ver') : ver })
    res = requests.get(url + queryParams)
    xml = res.text
    soup = BeautifulSoup(xml, 'html.parser')
    for tag in soup.find_all('stationname'):
        station.append(tag.text)
    for tag in soup.find_all('pm10value'):
        pm10.append(tag.text)
    res = dict(zip(station, pm10))
    return res


def check_air_2(request_station):
    dataTime = []
    pm10 = []
    url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty"
    returnType="xml"
    numOfRows="100"
    pageNo="1"
    ver="1.0"
    stationName = request_station
    dataTerm = "DAILY"
    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : serviceKeyDecoded, quote_plus('returnType') : returnType, quote_plus('numOfRows') : numOfRows, quote_plus('pageNo') : pageNo, quote_plus('stationName') : stationName, quote_plus('dataTerm') : dataTerm, quote_plus('ver') : ver })
    res = requests.get(url + queryParams)
    xml = res.text
    soup = BeautifulSoup(xml, features='xml')
    for tag in soup.find_all('dataTime'):
        dataTime.append(tag.text)
    for tag in soup.find_all('pm10Value'):
        pm10.append(tag.text)
    dataTime.reverse()
    pm10.reverse()
    res = dict(zip(dataTime, pm10))
    return res