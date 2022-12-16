from urllib.parse import urlencode, unquote, quote_plus
import requests
from bs4 import BeautifulSoup

serviceKey = "0eC9FQ3sjJfOFgDhUwnwj%2BtT2FBCBEKAJQV1RwtgxJxTEplfXC%2FuV7L%2BXIi2b5SnYsfikgaWL08KHczUyqqfjQ%3D%3D"
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')

def check_air(request):
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
    soup = BeautifulSoup(xml, 'xml')
    for tag in soup.find_all('dataTime'):
        dataTime.append(tag.text)
        
    for tag in soup.find_all('pm10Value'):
        pm10.append(tag.text)
        print(tag)
    dataTime.reverse()
    pm10.reverse()
    res = dict(zip(dataTime, pm10))
    print(dataTime)
    print(pm10)
    return res
# returnType=xml&numOfRows=100&pageNo=1&stationName=종로구&dataTerm=DAILY&ver=1.0
# returnType=xml&numOfRows=100&pageNo=1&sidoName=서울&ver=1.0