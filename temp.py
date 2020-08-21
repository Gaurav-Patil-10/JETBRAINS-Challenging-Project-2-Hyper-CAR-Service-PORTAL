


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
        

    
