# https://leetcode.com/problems/maximum-swap/ 

class Solution:
    def maximumSwap(self, num: int) -> int:
        strN = str(num)
        n = len(strN)        
        visited = [False for _ in range(n)]
        nums = [s for s in strN]
        idx = 0
        while idx < n:            
            arr = [(nums[i], i) for i in range(n) if visited[i] == False]
            maxElem, position = max(arr)
            
            if nums[idx] == maxElem: 
                visited[idx] = True
                idx += 1
            else: 
                nums[idx], nums[position] = nums[position], nums[idx] 
                break 
        
        return int("".join(nums))
