from django.shortcuts import render,HttpResponse
from .api import check_air

def main(request):
    
    return render(request,'index.html')
def charts(request):
    res = check_air()
    pm10 = res.get('다사읍')
    context = {'station' : '다사읍', 'pm10' : pm10}
    return render(request, 'everychart.html', context)