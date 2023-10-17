def majorityElement(arr) :
        num1 = -1
        num2 = -1

        count = 0
        count2 = 0

        for i in range(len(arr)):

            if arr[i] == num1:
                count+=1
            elif arr[i] == num2:
                count2+=1
            elif count ==0:
                num1 = arr[i]
                count = 1
            elif count2 ==0:
                num2 = arr[i]
                count2 =1
            else:
                count -=1
                count2-=1

        count = 0
        count2 = 0

        for i in range(len(arr)):
            if arr[i] == num1:
                count+=1
            elif arr[i] == num2:
                count2+=1
        
        if count > len(arr)/3 and count2 > len(arr)/3:
            return [num1,num2]
        
        
        if count > len(arr)/3:
            return [num1]
        
        
        if count2 > len(arr)/3:
            return [num2]
        
        return []
