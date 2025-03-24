from collections import deque
jug1 = int(input("Give jug 1 capacity :"))
jug2 = int(input("Give jug 2 capacity : "))
cap = int(input("Give source capacity : "))

visited = set()
q = deque()
q.append((0,0,[]))

while q :
    j1,j2,states = q.popleft()
    if(j1==jug1 and j2==jug2):
        states.append((j1,j2))
        print(states)
        break #ans found
    #this is to prevent already visited nodes and making it infinite
    if((j1,j2) in visited):
        continue
    visited.add(j1,j2)
    
    #actual logic
    moves = [
        [jug1 , j2 , "Fill jug1"] , 
        [j1 , jug2 , "Fill jug2"] , 
        [0 , j2 , "Empty jug1"], 
        [j1 , 0 , "Empty jug2"]
    ]
    