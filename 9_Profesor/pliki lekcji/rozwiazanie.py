def check_connection(a, b, conn):
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