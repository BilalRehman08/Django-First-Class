from django.http import HttpResponse


def secondappindex(request):
    return HttpResponse("Second App ==> Default Index")


def secondappfirstindex(request):
    return HttpResponse("Second App ==> First Index")


def secondappsecondindex(request):
    return HttpResponse("Second App ==> Second Index")


def secondappthirdindex(request):
    return HttpResponse("Second App ==> Third Index")
