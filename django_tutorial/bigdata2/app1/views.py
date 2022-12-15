from django.shortcuts import render, HttpResponseRedirect
from .api import check_air
sidoNames = {"서울":"서울",
            "충남":"충남",
            "제주":"제주",
            "전북":"전북",
            "전남":"전남",
            "인천":"인천",
            "울산":"울산",
            "세종":"세종",
            "충북":"서울",
            "부산":"부산",
            "대전":"대전",
            "대구":"대구",
            "광주":"광주",
            "경북":"경북",
            "경남":"경남",
            "경기":"경기",}




def first_page(request) :
    
    return render(request, 'app1/firstpage.html', {"sidoName":sidoNames})


def second_page(request):
    sidoName = request.GET.get('sidoName')
    station_pm10 = check_air(sidoName)
    # context = {
    #     'station_pm10' : station_pm10,
    #     'sidoName' : sidoNames
    # }
    return render(request, 'app1/secondpage.html', {'station_pm10' : station_pm10, 'sidoNames':sidoNames, 'sidoName' : sidoName,})


def final_page(request):
    sidoName = request.GET.get('sidoName')
    station_pm10 = check_air(sidoName)
    stationname = request.GET.get('stationName')
    return render(request, 'app1/finalpage.html', {'station_pm10' : station_pm10, 'sidoNames':sidoNames, 'sidoName' : sidoName,})