from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('firstindex', views.firstindex, name='firstindex'),
    path('secondindex', views.secondindex, name='secondindex'),
    path('thirdindex', views.thirdindex, name='thirdindex'),
]
