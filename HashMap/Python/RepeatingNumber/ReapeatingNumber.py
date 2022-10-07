
# Online Python - IDE, Editor, Compiler, Interpreter

def findRepetingNum(arr):
    
    dict = {}
    
    for i in range(0,len(arr)-1):
        if dict.get(arr[i]):
            return arr[i]
        else:
            dict[arr[i]] = 1
            
    return arr-1
    
    
print(findRepetingNum([1,3,2,3,4]))

# complexity O(n), time and space

    
