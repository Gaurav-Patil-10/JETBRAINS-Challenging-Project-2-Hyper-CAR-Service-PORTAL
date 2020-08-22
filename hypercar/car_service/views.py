from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

# Create your views here.

tickets_dict = {
    'oil': 0,
    'tire': 0,
    'diag': 0,
}

count_ticket = 1


def task_time(ticket):
    if 'oil' in ticket:
        return tickets_dict['oil'] * 2
    elif'tire' in ticket:
        return (tickets_dict['oil'] * 2) + (tickets_dict['tire'] * 5)
    elif 'diag' in ticket:
        return (tickets_dict['oil'] * 2) + (tickets_dict['tire'] * 5) + (
            tickets_dict['diag'] * 30)


def electronic_queue(client):

    global count_ticket
    busy_stage = False
    wait_time = task_time(client)

    if "oil" in client:
        tickets_dict['oil'] += 1
    elif 'tire' in client:
        tickets_dict['tire'] += 1
    elif 'diag' in client:
        tickets_dict['diag'] += 1

    if sum(tickets_dict.values()) > 2:
        busy_stage = True

    if busy_stage:
        count_ticket += 1

        return {
            'number' : count_ticket - 1,
            'wait' : wait_time
        }
        
    else:
        return {
            'number' : 0,
            'wait' : 0
        }
        

class MainPage(View):

    def get(self, requests, *args, **kwargs):

        return HttpResponse("<h2>Welcome to the Hypercar Service!</h2>")


class MenuPage (View):

    def get(self, requests, *args, **kwargs):
        return render(requests, 'menu.html')


class ServicePage (View):

  
    count_ticket = 1

    def get(self, requests, query, *args, **kwargs):

        client = electronic_queue(query)
        return render (requests , "service.html" , context={ "data" : client})


class Processing_Page (View):

    def get(self , requests , *args , **kwargs) :

        clients_queue = tickets_dict

        return render ( requests , "process.html" , context= {'line' : clients_queue})
        
