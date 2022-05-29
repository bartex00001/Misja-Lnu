from check_connection import check_connection
import random

def random_decision(probability):
    return random.randint(0, 100) < probability

def generateRandomData():
    dataSize = random.randint(3,12)
    connections = {}
    for stop in range(1,dataSize+1):
        connections[stop] = []

    for stop_a in range(1,dataSize+1):
        for stop_b in range(1,dataSize+1):
            # skip pairs
            if stop_a == stop_b:
                continue
            # Does this connection exist already?
            if stop_b in connections[stop_a]:
                # if so, continue
                continue
            # Randomize if we want conneciton here?
            decision = random_decision(25)
            if decision:
                connections[stop_a].append(stop_b)
                connections[stop_b].append(stop_a)

    stop_a, stop_b = random.sample(range(1, dataSize), 2)

    return stop_a, stop_b, connections

def correct_solution(a,b,conn):
    q = [ a ]
    visited = [False] * (len(conn)+1)
    while q:
        front = q.pop(0)
        for nb in conn[front]:
            if nb == b:
                return True
            if visited[nb]:
                continue
            visited[nb] = True
            q.append(nb)
    return False



def test():
    random_test = generateRandomData()
    print(random_test)
    try:
        wartosc = check_connection(random_test[0], random_test[1], random_test[2])
        oczekiwana = correct_solution(random_test[0], random_test[1], random_test[2])
        komunikat = f"check_connection( {random_test[0]}, {random_test[1]}, polaczenia[] ) = { str(wartosc) }; Poprawne: { bool(oczekiwana)  }"
        print(komunikat)
        return wartosc == oczekiwana
    except:
        komunikat = "Coś poszło nie tak..."
        print(komunikat)
        return False

test()