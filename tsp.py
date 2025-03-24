from itertools import permutations
def tsp(graph , cities):
    best = []
    minDist = float('inf')
    for perm in permutations(cities):
        from_city = 0 
        currentDist = 0 
        for to in perm:
            currentDist += graph[from_city][to]
            from_city = to
        currentDist += graph[from_city][0]
        
        if (currentDist < minDist) : 
            minDist = currentDist 
            best = perm
    print(f"The best path {perm}")
    return minDist    
graph = [
    [0, 10, 13, 17],
    [10, 0, 8, 6],
    [13, 8, 0, 10],
    [17, 6, 10, 0]
]
cities = [i for i in range(1, len(graph))] 
minDist = tsp(graph , cities )
print(f"The minimum distance is : {minDist}")   