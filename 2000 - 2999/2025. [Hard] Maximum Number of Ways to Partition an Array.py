# https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/

class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        prefix = [0]
        loc = defaultdict(lambda: [])
        
        for (i, num) in enumerate(nums):
            prefix.append(prefix[-1] + num)
            if i < len(nums) - 1:
                loc[prefix[-1]].append(i)
         
        ans = 0 
        if prefix[-1] % 2 == 0: 
            ans = len(loc[prefix[-1]//2])
            
        total = prefix[-1]
        
        for (i, num) in enumerate(nums):
            cnt = 0 
            diff = k - num
            target = total +  diff
            if target % 2 == 0: 
                target //= 2
                cnt = bisect_left(loc[target], i)
                cnt += len(loc[target-diff]) - bisect_left(loc[target-diff], i)
            ans = max(ans, cnt)
        
        return ans 
        
        
