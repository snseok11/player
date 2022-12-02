from django.shortcuts import render
from api import check_air
# Create your views here.
def index(request) :
    
    return render(request, 'templates/main.html')

def nowpm(request) :
    res=check_air()
    context = {'dust':res}
    return render(request,'templates/nowpm.html',context)