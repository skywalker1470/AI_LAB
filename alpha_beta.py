def pruning(depth , nodeIdx ,ismax ,  values , alpha , beta , branching_factor):
    if depth == 3: 
        return values[nodeIdx]
    
    if ismax:
        best = float('-inf')
        for i in range(branching_factor):
            val = pruning(depth+1 , nodeIdx *2 + i , False , values , alpha ,beta , branching_factor)
            best = max(val , best)
            alpha = max(alpha , best)
            if (beta <= alpha):
                break
        return best
    else:
        best = float('inf')
        for i in range(branching_factor):
            val = pruning(depth+1 , nodeIdx*2 + i , True , values , alpha , beta , branching_factor)
            best = min(val , best)
            beta = min(best , beta)
            if(beta<=alpha):
                break
        return best
#2^3 = 8
values = [1 , 2 ,-3 , 4, 10 , 8 ,5 , -1]
optimal_value = pruning (0 , 0 , True , values , float('-inf') , float('inf') , 2)
print(optimal_value)
    