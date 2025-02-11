from collections import deque


def solution(tickets):
    allroute = []
    queue = deque([("ICN", ["ICN"])])
    visit = []
    while queue:
        locate, Troute = queue.popleft()

        if len(visit) == len(tickets):
            allroute.append(Troute)

        ableroute = []
        for ticket in tickets:
            if ticket[0] == locate and ticket not in visit:
                ableroute.append(ticket)
                Troute.append(ticket[1])
                queue.append([ticket[1], Troute])
                visit.append(ticket)

        if 0 < len(ableroute) and len(ableroute) > 1:
            sorted(ableroute, key=lambda x: x[1])
            print(ableroute)
            ticket = ableroute[0]
            Troute.append(ticket[1])
            queue.append([ticket[1], Troute])
            visit.append(ticket)
        else:
            ticket = ableroute[0]
            Troute.append(ticket[1])
            queue.append([ticket[1], Troute])
            visit.append(ticket)

    # if len(allroute) == 1:
    #     return allroute[0]
    # else:
    #     return allroute[0]

    return -1