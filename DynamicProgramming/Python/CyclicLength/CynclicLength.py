
cache = {}
def cyclicLength(i,j):
    totalCount = 0
    while i >= j:
        count = 1
        val  = i
        while val != 1:
            if cache.get(val) != None:
                count += cache[val] - 1
                break
            count +=1
            if val % 2 == 0:
                val = val/2
            else:
                val = (3*val + 1)
        
        cache[i] = count
        totalCount = max(count,totalCount)
        i-=1
    return totalCount;
    
arr = [ [10,1],[200,100],[210,201],[1000,900],[1000000,1],[5,1],[22232,254]]

for i in range(len(arr)):
    
    print(cyclicLength(arr[i][0],arr[i][1]))
        