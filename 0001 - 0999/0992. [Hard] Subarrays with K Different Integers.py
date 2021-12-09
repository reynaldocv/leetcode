# https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(m):
            counter = defaultdict(lambda: 0)
            ans = idx = 0 
            
            for (i, num) in enumerate(nums):
                counter[num] += 1
                
                while len(counter) > m: 
                    counter[nums[idx]] -= 1
                    if counter[nums[idx]] == 0:
                        counter.pop(nums[idx])
                    idx += 1
                
                ans  += i - idx + 1
                
            return ans
                
        return helper(k) - helper(k - 1)
                
        
                    
                    
