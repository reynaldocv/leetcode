# https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/

class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums) 
        
        index = defaultdict(lambda: [])
        
        for (i, num) in enumerate(nums):
            index[num].append(i)
            
        ans = inf
            
        for key in index: 
            m = len(index[key])
            if m == 1:
                ans = min(ans, (n//2))
                
            else: 
                tmp = 0 
                
                for i in range(m):
                    if i == 0: 
                        tmp = max(tmp, (index[key][0] + n - index[key][-1])//2)
                        
                    else:
                        tmp = max(tmp, (index[key][i] - index[key][i - 1])//2)
                
                ans = min(ans, tmp)
                
        return ans 
                      
