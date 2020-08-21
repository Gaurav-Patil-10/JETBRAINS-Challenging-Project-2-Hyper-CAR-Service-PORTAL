

oil_clients = []
tire_clients = []
diag_clients = []


def wait_time(ticket):
    if "oil" in ticket:
        return oil_clients[-1]['wait time'] + 2

    elif "tire" in ticket:
        time = tire_clients[-1]['wait time'] + 5

        return time

    elif "diag" in ticket:
        time = diag_clients[-1]['wait time'] + 30
        return time


while True:

    client = input("Enter the job : ")

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
                "wait time": wait_time("oil")
            }
            oil_clients.append(client_dict)

    elif "tire" in client:

        if tire_clients == [] and oil_clients != []:
            client_dict = {
                "id":  oil_clients[-1]['id'] + 1 ,
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
                "wait time": wait_time("tire")
            }
            tire_clients.append(client_dict)

    elif "diag" in client:

        if tire_clients == [] and diag_clients == [] and oil_clients == []:
            client_dict = {
                "id": 1,
                "wait time": 0
            }
            diag_clients.append(client_dict)

        elif tire_clients != [] and oil_clients != [] and diag_clients != []:
            client_dict = {
                "id": diag_clients[-1]['id'] + 1,
                "wait time": wait_time("diag")
            }
            diag_clients.append(client_dict)
        
        elif tire_clients != [] and oil_clients != [] and diag_clients == []:
            client_dict = {
                "id": tire_clients[-1]['id'] + 1 ,
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
                    "id": oil_clients[-1]['id'] + 1 ,
                    "wait time": oil_clients[-1]['wait time'] + 30
                }
                diag_clients.append(client_dict)

            elif oil_clients == [] and tire_clients == [] and diag_clients != []:
                client_dict = {
                    "id": diag_clients[-1]['id'] + 1,
                    "wait time": diag_clients[-1]['wait time'] + 30
                }
                diag_clients.append(client_dict)

    print(oil_clients)
    print(tire_clients)
    print(diag_clients)
