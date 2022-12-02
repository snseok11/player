from urllib.parse import urlencode, unquote, quote_plus
import requests
from bs4 import BeautifulSoup

serviceKey = ""
servicekeyDecoded = unquote(serviceKey, 'UTF-8')

def check_air():
    station = []
    pm10 = []
    url="https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
    return_type="xml"
    num_of_rows="100"
    page_no="1"
    sido_name="대구"
    ver="1.0"
    queryParams = "?" + urlencode({quote_plus('serviceKey') : servicekeyDecoded, quote_plus('returnType') :return_type, quote_plus('numOfRows') : num_of_rows, quote_plus('pageNo') :page_no, quote_plus('sidoName'): sido_name, quote_plus('ver') : ver})
    
    res = requests.get(url + queryParams)
    xml = res.text
    soup = BeautifulSoup(xml, 'html.parser')
    for tag in soup.find_all('stationname'):
        station.append(tag.text)
    for tag in soup.find_all('pm10value'):
        pm10.append(tag.text)
    res = dict(zip(station, pm10))
    return res