from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Welcome to the meltex homepage")

def get_listings(request):
    return HttpResponse("Welcome to the listings page")

def add_listing(request):
    return HttpResponse("Welcome to the add listing page")
