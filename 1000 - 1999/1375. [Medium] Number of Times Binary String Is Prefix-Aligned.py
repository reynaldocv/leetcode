# https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        maxElem = 0 
        aSum = 0 
        ans = 0 
        
        for num in light:
            aSum += num
            maxElem = max(maxElem, num)
            if maxElem*(maxElem + 1)//2 == aSum:
                ans += 1 
                
        return ans    

class Solution2:
    def numTimesAllBlue(self, light: List[int]) -> int:
        n = len(light)
        seen = {i + 1: True for i in range(n)}
        heap = [i + 1 for i in range(n)]
        
        ans = 0 
        for (i, idx) in enumerate(light):
            seen.pop(idx)
            while heap and heap[0] not in seen:
                heappop(heap)
                
            if heap and heap[0] > i + 1: 
                ans += 1 
                 
        return ans + 1
