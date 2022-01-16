from django.http import HttpResponse


def index(request):
    return HttpResponse("first app ==> Default index")


def firstindex(request):
    return HttpResponse("first app ==> first index")


def secondindex(request):
    return HttpResponse("first app ==> second index")


def thirdindex(request):
    return HttpResponse("first app ==> third index")
