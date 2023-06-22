# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = defaultdict(lambda: 0)
        
        maxCounter = 0
        
        
        for num in nums: 
            counter[num] += 1 
            
            maxCounter = max(maxCounter, counter[num])
            
        ans = [[] for _ in range(maxCounter)]
        
        for key in counter:
            for i in range(counter[key]):
                ans[i].append(key)
                
        return ans 
