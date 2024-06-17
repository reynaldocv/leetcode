# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counter = defaultdict(lambda: 0)
        
        for num in power: 
            counter[num] += num
            
        nums = sorted([key for key in counter])
        
        arr = [-3]
        dp = [0]
        
        for num in nums: 
            value = num - 2
            
            idx = bisect_left(arr, value) - 1
            
            arr.append(num)
            dp.append(max(dp[-1], dp[idx] + counter[num]))
   
        return max(dp)
