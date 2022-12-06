from django.shortcuts import render
from .api import check_air
# Create your views here.
def index(request) :
    res = check_air()
    pm10 = res.get('다사읍')
    context = {'station' : '다사읍', 'pm10' : pm10}
    return (render(request, 'dust_checker/dust_main.html'))