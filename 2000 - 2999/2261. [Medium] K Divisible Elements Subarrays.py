# https://leetcode.com/problems/k-divisible-elements-subarrays/

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        seen = set()
        
        for (i, arr) in enumerate(nums):
            counter = 0         
            key = ()
            for num in nums[i: ]:
                if num % p == 0: 
                    counter += 1 
                    
                if counter > k: 
                    break 
                else: 
                    key = key + (num, )
                    seen.add(key)

        return len(seen)
                    
                
            
