from django.urls import path

from . import views

urlpatterns = [
    path('', views.secondappindex, name='index'),
    path('firstindex', views.secondappfirstindex, name='firstindex'),
    path('secondindex', views.secondappsecondindex, name='secondindex'),
    path('thirdindex', views.secondappthirdindex, name='thirdindex'),
]
