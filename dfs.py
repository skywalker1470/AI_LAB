
def dfs(graph ,start):
    stack = deque([start])
    visited = set([start])
    
    while stack:
        node = stack.pop()
        print(node , end=" ")
        for neigh in graph[node]:
            if neigh not in visited:
                visited.add(neigh)
                stack.append(neigh)
                
graph = {
    0 : [1 ,2 ] , 
    1 : [0],
    2 : [0 , 3 ,4 ],
    3:  [2 , 5],
    4: [2],
    5:[3]
}
dfs(graph , 0)