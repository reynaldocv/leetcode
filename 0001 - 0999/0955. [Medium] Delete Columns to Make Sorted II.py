# https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def helper(strs, idx = 0):
            if strs == sorted(strs):
                return 0 
            else: 
                prefix = [s[:idx + 1] for s in strs]
                if prefix == sorted(prefix):
                    return helper(strs, idx + 1)
                else:
                    newStrs = [s[:idx] + s[idx + 1:] for s in strs]
                    return 1 + helper(newStrs, idx)

        return  helper(strs)
        
