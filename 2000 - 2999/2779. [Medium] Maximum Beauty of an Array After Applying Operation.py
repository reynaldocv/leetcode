# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        counter = defaultdict(lambda: 0)
        
        for num in nums: 
            counter[num - k] += 1 
            counter[num + k + 1] -= 1 
            
        coordX = [key for key in counter]
        coordX.sort() 
        
        ans = prev = 0 
        
        for x in coordX: 
            prev += counter[x]
            
            ans = max(ans, prev)
            
        return ans 
            
