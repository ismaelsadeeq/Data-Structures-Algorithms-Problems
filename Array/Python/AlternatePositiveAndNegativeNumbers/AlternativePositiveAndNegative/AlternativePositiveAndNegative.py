    def rearrange(self,arr, n):
        
        positiveArr = []
        negativeArr = []
        for i in range(0,len(arr)):
            if(arr[i]<0):
                negativeArr.append(arr[i])
            else:
                positiveArr.append(arr[i])
        
        negativeIndex = 0
        positiveIndex = 0
        
        for i in range(0,len(arr)):
            
            if i % 2 == 0 :
                
                if positiveIndex < len(positiveArr):
                    arr[i] = positiveArr[positiveIndex]
                    positiveIndex+=1
                else:
                    arr[i] = negativeArr[negativeIndex]
                    negativeIndex +=1
            else:
                
                if negativeIndex < len(negativeArr):
                    arr[i] = negativeArr[negativeIndex]
                    negativeIndex+=1
                else:
                    arr[i] = positiveArr[positiveIndex]
                    positiveIndex+=1
        
        return arr


    