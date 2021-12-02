# https://leetcode.com/problems/k-th-smallest-prime-fraction/

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        aux = []
        
        arr.sort()        
        n = len(arr)
        
        for (i, num) in enumerate(arr):
            for j in range(i + 1, n):
                aux.append((num, arr[j]))
                
        aux.sort(key = lambda item: item[0]/item[1])
        
        return aux[k - 1]
        
class Solution2:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        def helper(x):
            j, p, q = 0, 0, 1
            counter = 0
            for i in range(n):
                while j < n and arr[i]/arr[j] > x: 
                    j += 1
                
                if j < n and p/q < arr[i]/arr[j]: 
                    p, q = arr[i], arr[j]
                    
                counter += n - j
                
            return counter, p, q
            
        start, end = 0, 1
        
        n = len(arr)
        
        while end > start: 
            middle = (end + start)/2
            counter, p, q = helper(middle)
            if counter > k: 
                end = middle
            elif counter < k: 
                start = middle
            else: 
                return [p, q]
        
