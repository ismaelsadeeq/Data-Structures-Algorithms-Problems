    def assign (self, arr,  n) : 
        #Complete the function
        
        arr.sort()
        half = 0
        if n % 2 ==0:
            half  = (n/2) -1
        else:
            half = n//2
        
        l = []
        h = []
        myArr = []
        for i in range (n):
            if i <= half:
                l.append(arr[i])
            else:
                h.append(arr[i])
            
            myArr.append(0)
        length = 0
        i = 0
        while(i!=n and length < len(l)):
            myArr[i]= l[length]
            length+=1
            i+=2
        
        length = len(h)-1
        i = 1
        while(i!=n and length>=0):
            myArr[i] = h[length]
            length-=1
            i+=2
        return myArr
        