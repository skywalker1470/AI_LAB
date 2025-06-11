def water_jug (cap_a , cap_b , target):
    a = 0 
    b  = 0
    visited = set()

    while True:
        if (a,b) in visited:
            print("Loop detected ! No solution !")
            break
        visited.add((a,b))
        if(a==target or b==target):
            print("Target amount measured !!")
            break
        if(a==0):
            a = cap_a
            print("Fill jug A")
        elif(b==cap_b):
            b = 0
            print("Empty jug B")
        else:
            transfer = min (a , cap_b - b)
            a -= transfer
            b += transfer
            print(f"Transfer {transfer}L from A to B")
        
    return

        
        
cap_a = int(input("Enter the Jug A capacity: "))
cap_b = int(input("Enter the Jug B capacity: "))
target = int(input("Enter the traget capacity: "))
water_jug(cap_a , cap_b , target)   
