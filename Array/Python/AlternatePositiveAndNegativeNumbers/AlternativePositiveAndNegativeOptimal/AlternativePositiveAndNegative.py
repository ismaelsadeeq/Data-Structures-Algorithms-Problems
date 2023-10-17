    def rearrange(self,arr, n):
        
        part = -1
        
        for i in range(0,len(arr)):
            if arr[i]<0:
               part+=1
               x = arr[i]
               y=arr[part]
               arr[i] = y
               arr[part] = x
        
        
        neg = 0
        part+=1
        while neg < part:
            x = arr[neg]
            y = arr[part]
            arr[neg] = y
            arr[part] = x
            neg+=2
            part+=1
      
        return arr



    