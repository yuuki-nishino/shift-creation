from django.http import HttpResponse


def index(request):
    return HttpResponse("We will make the web site for shift creation.")