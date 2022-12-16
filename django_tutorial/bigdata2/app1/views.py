from django.shortcuts import render, HttpResponseRedirect
from .api import check_air
from .api import check_air_2
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
            "경기":"경기",
}

def first_page(request) :
    return render(request, 'app1/firstpage.html', {"sidoNames":sidoNames})

def second_page(request):
    selected_sidoName = request.GET.get('select_sidoName')
    selected_sido_statioins_pm10= check_air(selected_sidoName)
    if request.GET.get('selected_stationName') == '' :
        return render(request, 'app1/secondpage.html', {'sidoNames': sidoNames, 'selected_sidoName' : selected_sidoName, 'selected_sido_stations_pm10' : selected_sido_statioins_pm10 })
    else : 
        selected_stationName = request.GET.get('selected_stationName')
        selected_station_data_pm10 = check_air_2(selected_stationName)
        #print(selected_station_data_pm10)
        return render(request, 'app1/finalpage.html', {'sidoNames': sidoNames, 'selected_sidoName' : selected_sidoName, 'selected_sido_stations_pm10' : selected_sido_statioins_pm10, 'selected_stationName' : selected_stationName, 'selected_station_data_pm10' : selected_station_data_pm10})