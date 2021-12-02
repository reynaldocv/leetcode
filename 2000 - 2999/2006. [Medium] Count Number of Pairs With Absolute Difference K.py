#  https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        counter = {}
        for num in nums: 
            counter[num] = counter.get(num, 0) + 1
        
        ans = 0 
        for key in counter: 
            ans += counter[key]*counter.get(key - k, 0)
            
        return ans
        
