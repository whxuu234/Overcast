# Inside your 'authentication' app

# views.py
from django.shortcuts import render
from django.http import HttpResponse

class PageViews:
    
    def front_page(request):
        return HttpResponse("This the front page.")
