from collections import deque
def dfs(graph , start):
    vis = set() 
    stack = deque([start])
    while stack:
        node = stack.pop()
        if node not in vis:
            vis.add(node)
            print(node , end = " ")
        for current in reversed(graph[node]):
            if current not in vis:
                stack.append(current)
#adj list
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

dfs(graph , 0)