from itertools import permutations

def tsp(graph , start , cities):
   
    minDist = float("inf") 
    best_path = []
    for perm in permutations(cities):
        from_city = start
        dist = 0 
        for to_city in perm:
            dist = graph[from_city][to_city]
            from_city = to_city
        
        dist += graph[from_city][start]
        if(dist<minDist):
            minDist = dist
            best_path = perm
    #pls format the output i am too sleepy to format fml
    print(f"{minDist} , 0-->{best_path}-->0")
    return

graph =[
    [0, 10, 13, 17],
    [10, 0, 8, 6],
    [13, 8, 0, 10],
    [17, 6, 10, 0]
]
cities = []
for i in range(1,4):
    cities.append(i)
tsp(graph , 0 , cities)