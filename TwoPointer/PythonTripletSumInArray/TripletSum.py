 #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    def find3Numbers(self,A, n, x):
        # Your Code Here
        A.sort()
        
        for i in range(0,n-1):
            
            left = i+1
            right = n-1
            
            while(left<right):
                sum = A[i] + A[left] + A[right]
                if sum == x:
                    return 1
                elif sum > x:
                    right-=1
                elif sum < x:
                    left+=1
                    
        return 0

        