from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

# Create your views here.

oil_clients = []
tire_clients = []
diag_clients = []

def wait_time(oil_clients , tire_clients , diag_clients , ticket):


    if "oil" in ticket:
        return oil_clients[-1]['wait time'] + 2

    elif "tire" in ticket:
        time = tire_clients[-1]['wait time'] + 5

        return time

    elif "diag" in ticket:
        time = diag_clients[-1]['wait time'] + 30
        return time


def electronic_que( oil_clients , tire_clients , diag_clients ,client):

    
    if "oil" in client:
        if oil_clients == []:
            client_dict = {
                "id": 1,
                "wait time": 2
            }
            oil_clients.append(client_dict)
        else:
            client_dict = {
                "id": oil_clients[-1]['id'] + 1,
                "wait time": wait_time(oil_clients , tire_clients , diag_clients ,"oil")
            }
            oil_clients.append(client_dict)

    elif "tire" in client:

        if tire_clients == [] and oil_clients != []:
            client_dict = {
                "id": oil_clients[-1]['id'] + 1,
                "wait time": oil_clients[-1]['wait time'] + 5
            }
            tire_clients.append(client_dict)

        elif tire_clients == [] and oil_clients == []:
            client_dict = {
                "id": 1,
                "wait time": 5
            }
            tire_clients.append(client_dict)

        elif tire_clients != []:
            client_dict = {
                "id": tire_clients[-1]['id'] + 1,
                "wait time": wait_time(oil_clients , tire_clients , diag_clients , "tire")
            }
            tire_clients.append(client_dict)

    elif "diag" in client:

        if tire_clients == [] and diag_clients == [] and oil_clients == []:
            client_dict = {
                "id": 1,
                "wait time": 30
            }
            diag_clients.append(client_dict)

        elif tire_clients != [] and oil_clients != [] and diag_clients != []:
            client_dict = {
                "id": diag_clients[-1]['id'] + 1,
                "wait time": wait_time(oil_clients , tire_clients , diag_clients , "diag")
            }
            diag_clients.append(client_dict)

        elif tire_clients != [] and oil_clients != [] and diag_clients == []:
            client_dict = {
                "id": tire_clients[-1]['id'] + 1,
                "wait time": tire_clients[-1]['wait time'] + 30
            }
            diag_clients.append(client_dict)

        else:
            if oil_clients == [] and tire_clients != [] and diag_clients == []:
                client_dict = {
                    "id": tire_clients[-1]['id'] + 1,
                    "wait time": tire_clients[-1]['wait time'] + 30
                }
                diag_clients.append(client_dict)

            elif oil_clients != [] and tire_clients == [] and diag_clients == []:
                client_dict = {
                    "id": oil_clients[-1]['id'] + 1,
                    "wait time": oil_clients[-1]['wait time'] + 30
                }
                diag_clients.append(client_dict)
            elif oil_clients == [] and tire_clients == [] and diag_clients != []:
                client_dict = {
                    "id": diag_clients[-1]['id'] + 1,
                    "wait time": diag_clients[-1]['wait time'] + 30
                }
                diag_clients.append(client_dict)

    new = oil_clients + tire_clients + diag_clients

    return new

        

class MainPage(View):

    def get(self, requests, *args, **kwargs):

        return HttpResponse("<h2>Welcome to the Hypercar Service!</h2>")


class MenuPage (View):

    def get(self, requests, *args, **kwargs):
        return render(requests, 'menu.html')


class ServicePage (View):

    oil_clients = []
    tire_clients = []
    diag_clients = []


    def get(self, requests, query, *args, **kwargs):

        client_list = electronic_que(oil_clients  , tire_clients , diag_clients , query)

        # new_list = sorted(client_list , key = int(client_list['wait time']) , reverse = False)
        new_list = client_list

        client = {
            'number' : new_list[-1]['id'],
            'wait' : new_list[-1]['wait time']
        }
        return render (requests , "service.html" , context={ "data" : client})
