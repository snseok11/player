
from django.urls import path
from . import views

app_name = 'app1'
urlpatterns = [
    path('', views.first_page, name="first"),
    path('second/', views.second_page, name="second"),
   # path('test_1/', views.test_1, name="test_1"),
    #path('test_2/', views.test_2, name="test_2"),
]
