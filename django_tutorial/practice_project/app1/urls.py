
from django.urls import path
from . import views

app_name ='app1'

urlpatterns = [
    path('', views.main, name='main'),
    path('ChartView/', views.charts, name='charts')
]
