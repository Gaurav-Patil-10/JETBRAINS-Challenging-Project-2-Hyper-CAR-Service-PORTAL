from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import HttpResponse
from collections import deque
# Create your views here.

tickets_dict = {
    'oil': deque(),
    'tire': deque(),
    'diag': deque(),
}

first_clients = []

current_client = None
count_ticket = 1


def initial_wait_time():

    global first_clients

    for x in first_clients:
        if "oil" in x['ticket name']:
            wait_time = 2
            break
        elif "tire" in x['ticket name']:
            wait_time = 5
    else:
        wait_time = 30

    return wait_time


def final_wait_time(query):

    global tickets_dict

    if "oil" in query:
        return len(tickets_dict['oil']) * 2

    elif "tire" in query:

        return (len(tickets_dict['oil']) * 2) + (len(tickets_dict['tire']) * 5)

    elif "diag" in query:
        return (len(tickets_dict['oil']) * 2) + (len(tickets_dict['tire']) * 5) + (len(tickets_dict['diag']) * 30)


class MainPage(View):

    def get(self, requests, *args, **kwargs):

        return HttpResponse("<h2>Welcome to the Hypercar Service!</h2>")


class MenuPage (View):

    def get(self, requests, *args, **kwargs):
        return render(requests, 'menu.html')


class ServicePage (View):

    def get(self, requests, query, *args, **kwargs):

        global count_ticket, first_clients, tickets_dict

        if count_ticket <= 2:
            first_clients.append({
                "id": 0,
                "wait time": 0,
                "ticket name": query
            })

            client = {
                'number': 0,
                'wait': 0
            }

        else:
            if count_ticket == 3:
                if "oil" in query:
                    tickets_dict['oil'].append({
                        'id': count_ticket - 2,
                        'wait time': initial_wait_time()
                    })
                elif "tire" in query:
                    tickets_dict['tire'].append({
                        'id': count_ticket - 2,
                        'wait time': initial_wait_time()
                    })
                elif "diag" in query:
                    tickets_dict['diag'].append({
                        'id': count_ticket - 2,
                        'wait time': initial_wait_time()
                    })

                client = {
                    'number': count_ticket - 2,
                    'wait': initial_wait_time()
                }
            else:
                if "oil" in query:
                    tickets_dict['oil'].append({
                        'id': count_ticket - 2,
                        'wait time': final_wait_time(query)
                    })
                elif "tire" in query:
                    tickets_dict['tire'].append({
                        'id': count_ticket - 2,
                        'wait time': final_wait_time(query)
                    })
                elif "diag" in query:
                    tickets_dict['diag'].append({
                        'id': count_ticket - 2,
                        'wait time': final_wait_time(query)
                    })

                client = {
                    'number': count_ticket - 2,
                    'wait': final_wait_time(query)
                }
        count_ticket += 1
        # print(client)
        # print(tickets_dict)
        return render(requests, "service.html", context={"data": client})


class Processing_Page (View):

    def get(self, requests, *args, **kwargs):

        global count_ticket, first_clients, tickets_dict

        new_dict = {
            'oil': 0,
            'tire': 0,
            'diag': 0
        }

        for x in first_clients:
            if "oil" in x['ticket name']:
                new_dict['oil'] += 1
            elif "tire" in x['ticket name']:
                new_dict['tire'] += 1
            elif "diag" in x['ticket name']:
                new_dict['diag'] += 1

        print(first_clients)
        print(new_dict)

        new_dict['oil'] += len(tickets_dict['oil'])
        new_dict['tire'] += len(tickets_dict['tire'])
        new_dict['diag'] += len(tickets_dict['diag'])

        print(new_dict)

        return render(requests, "process.html", context={'line': new_dict})

    def post(self, requests, *args, **kwargs):

        global count_ticket, first_clients, tickets_dict, current_client

        if len(tickets_dict['oil']) != 0:
            current_client = tickets_dict['oil'].popleft()

        elif len(tickets_dict['oil']) == 0 and len(tickets_dict['tire']) != 0:
            current_client = tickets_dict['tire'].popleft()

        elif len(tickets_dict['oil']) == 0 and len(tickets_dict['tire']) == 0 and len(tickets_dict['diag']) != 0:
            current_client = tickets_dict['diag'].popleft()

        elif len(tickets_dict['oil']) == 0 and len(tickets_dict['tire']) == 0 and len(tickets_dict['diag']) == 0:
            current_client = None

        return redirect("/next")


class Next_Client (View):

    def get(self, requests, *args, **kwargs):

        global current_client

        if current_client == None:
            client = False
        else:
            client = current_client

        return render(requests, 'next.html', context={'clients': client})
