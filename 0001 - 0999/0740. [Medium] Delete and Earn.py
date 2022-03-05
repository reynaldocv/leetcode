# https://leetcode.com/problems/delete-and-earn/

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        maxElem = max(nums)
        arr = [0 for i in range(maxElem + 1)]
        
        counter = defaultdict(lambda: 0)
        for num in nums: 
            counter[num] += 1 
        
        for num in range(1, maxElem + 1):
            arr[num] = max(arr[num - 1], arr[num - 2] + counter[num]*num)
            
        return arr[-1]
            
            
        
        
        

        
            
        
