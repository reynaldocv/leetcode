#  https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        counter = defaultdict(lambda: 0)
                              
        for num in nums: 
            counter[num] += 1
        
        ans = 0 
                              
        for key in counter: 
            if key - k in counter: 
                ans += counter[key]*counter[key - k]
            
        return ans

class Solution2:
    def countKDifference(self, nums: List[int], k: int) -> int:
        counter = defaultdict(lambda: 0)
        
        nums.sort() 
        
        ans = 0 
        
        for num in nums: 
            ans += counter[num - k]
            
            counter[num] += 1 
            
        return ans 
            
        
        
