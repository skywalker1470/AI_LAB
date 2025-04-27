def water_jug (cap_a , cap_b  , target):
    a , b = 0 , 0
    steps = 0
    while True:
        print(f"Step {steps}: Jug A = {a} liters, Jug B = {b} liters")
        if a == target or b == target:
            print("Goal achieved!")
            break
        if a == 0:
            a = cap_a
            print(f"Fill Jug A to {cap_a} liters.")
        elif b == cap_b:
            b = 0
            print(f"Empty Jug B.")
        else:
            transfer = min(a, cap_b - b)
            a -= transfer
            b += transfer
            print(f"Pour {transfer} liters from Jug A to Jug B.")

        steps += 1
        
        
cap_a = int(input("Enter the Jug A capacity: "))
cap_b = int(input("Enter the Jug B capacity: "))
target = int(input("Enter the traget capacity: "))
water_jug(cap_a , cap_b , target)   
