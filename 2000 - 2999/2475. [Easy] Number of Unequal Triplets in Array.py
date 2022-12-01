# https://leetcode.com/problems/number-of-unequal-triplets-in-array/

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        counter = defaultdict(lambda: 0)
        
        for num in nums: 
            counter[num] += 1 
            
            
        arr = [key for key in counter]
        
        ans = 0 
        
        for (a, b, c) in combinations(arr, 3):
            ans += counter[a]*counter[b]*counter[c]
            
        return ans
    
