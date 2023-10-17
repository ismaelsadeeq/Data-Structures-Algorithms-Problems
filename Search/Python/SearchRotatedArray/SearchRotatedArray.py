
class Solution:
    def search(self, A : list, l : int, h : int, key : int):
        # l: The starting index
        # h: The ending index, you have to search the key in this range
        # Complete this function
        pivot = Solution.searchPivot(A,l,h)
        if key > A[h-1]:
            return Solution.binarySearch(A,l,pivot,key)
        else:
            return Solution.binarySearch(A,pivot,h,key)
    
    def binarySearch(arr,start,end,key):
        
        if start > end :
            return -1
        mid = (end + start) //  2
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            return Solution.binarySearch(arr,start,mid-1,key)
        else:
            return Solution.binarySearch(arr,mid+1,end,key)
            
    def searchPivot(A,l,h):
        
        if(l>h):
            return -1
        if l==h:
            return l
        
        mid = (h+l) //2
      
        if A[mid] < A[mid-1]:
            return mid
            
        if A[mid] > A[mid+1]:
            return mid+1
        
        if A[l] > A[mid]:
            return Solution.searchPivot(A,l,mid-1)
            
        return Solution.searchPivot(A,mid+1,h)
            