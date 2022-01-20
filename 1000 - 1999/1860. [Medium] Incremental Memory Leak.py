# https://leetcode.com/problems/incremental-memory-leak/

class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        ans = [1, memory1, memory2]
        
        while ans[0] <= ans[1] or ans[0] <= ans[2]:
            if ans[0] <= ans[1] and ans[1] >= ans[2]:
                ans[1] -= ans[0]
            else:
                ans[2] -= ans[0]
        
            ans[0] += 1
        
        return ans
        
