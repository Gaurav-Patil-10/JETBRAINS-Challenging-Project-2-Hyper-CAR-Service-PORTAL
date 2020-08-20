from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

# Create your views here.

class MainPage(View):


    def get(self, requests , *args , **kwargs):

        return HttpResponse ("<h2>Welcome to the Hypercar Service!</h2>")


class MenuPage (View):

    def get(self , requests , *args, **kwargs):
        return render ( requests , 'menu.html')