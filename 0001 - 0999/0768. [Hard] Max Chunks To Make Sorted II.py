# https://leetcode.com/problems/max-chunks-to-make-sorted-ii/

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        
        maximum = [0 for _ in range(n)]
        maximum[0] = arr[0]
        
        minimum = [0 for _ in range(n)]
        minimum[-1] = arr[-1]
        
        for i in range(1, n):
            maximum[i] = max(arr[i], maximum[i - 1])
            minimum[n - 1 - i] = min(arr[n - 1 - i], minimum[n - i])
        
        ans = 0 
        
        for i in range(n - 1):
            if maximum[i] <= minimum[i + 1]:
                ans += 1 
                
        return ans + 1
      
 class Solution2:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sortedArr = sorted(arr)
        aux = []
        ans = 0 
        
        for (i, num) in enumerate(arr): 
            insort(aux, num)
            if aux == sortedArr[: i + 1]:
                ans += 1 
            
        return ans
