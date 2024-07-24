# https://leetcode.com/problems/destroy-sequential-targets/

class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        counter = defaultdict(lambda: 0)
        
        nums.sort() 
        
        for num in nums: 
            counter[num % space] += 1 
            
        cnt = defaultdict(lambda: 0)
        
        ans = (0, 0)
        
        for num in nums: 
            tmp = num % space
            
            ans = max(ans, (counter[tmp] - cnt[tmp], -num))
            
            cnt[tmp] += 1 
            
        return -ans[1]
            
