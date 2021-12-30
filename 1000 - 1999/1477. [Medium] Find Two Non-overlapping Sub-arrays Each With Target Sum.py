# https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        def helper(arr):
            ans = [inf for _ in range(n)]
            prev = 0         
            seen = {prev: -1}
            
            for (i, num) in enumerate(arr): 
                prev += num
                aux = prev - target
                if aux not in seen: 
                    ans[i] = ans[i - 1]
                elif i == 0: 
                    ans[i] = i - seen[aux]
                else:
                    ans[i] = min(i - seen[aux], ans[i - 1])
                
                seen[prev] = i
            
            return ans 
        
        n = len(arr)
        
        left = helper(arr)
        right = helper(arr[::-1])[::-1]
        
        ans = inf
        for i in range(n):
            prefix = inf if i == 0 else left[i - 1]
            suffix = right[i]
            ans = min(ans, prefix + suffix)
            
        return ans if ans != inf else -1
