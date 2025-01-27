from collections import deque 
#adjacency list
def bfs(graph , start) : 
    q = deque([start])
    visited = set([start])
    while q:
        node = q.popleft()
        print(node , end=" ")
        for neigh in graph[node]:
            if neigh not in visited:
                visited.add(neigh)
                q.append(neigh)


graph = { 
    0:[1,2],
    1:[0,5,3],
    2:[3,0],
    3:[1,2,5],
    4:[7],
    5:[1,3,6],
    6:[5,7],
    7:[3,4,6],
}

start = 0 

bfs(graph , start )