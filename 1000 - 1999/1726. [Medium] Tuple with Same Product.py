# https://leetcode.com/problems/tuple-with-same-product/

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        counter = defaultdict(lambda: 0)
        
        for (i, numA) in enumerate(nums):
            for numB in nums[i + 1:]:
                counter[numA*numB] += 1
            
        ans = 0
        for key in counter: 
            if counter[key] > 1:
                ans += 4*(counter[key] - 1)*counter[key]
                
        return ans
                
        
        
