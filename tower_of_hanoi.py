def hanoi(n,source,middle,dest):
    if(n==1):
        print(f"Move disk {n} to {source} -> {dest}")
        return
    hanoi(n-1 , source , dest , middle)
    print(f"Move disk {n} to {source} -> {dest}")
    hanoi(n-1 , middle , source  , dest)
    return

n = int(input("How many disks? :"))
hanoi(n , 'A' , 'B' , 'C')
