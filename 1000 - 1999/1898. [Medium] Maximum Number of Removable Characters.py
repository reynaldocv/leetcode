# https://leetcode.com/problems/maximum-number-of-removable-characters/

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def helper(m):
            i = j = 0
            remove = set(removable[:m+1])
            while i < len(s) and j < len(p):
                if i not in remove and s[i] == p[j]:
                    j += 1
                i += 1
            
            return j == len(p)
            
        n = len(removable)
        start = -1
        end = n
        
        while end - start > 1:
            mid = (end + start) // 2
            if helper(mid):
                start = mid                
            else:
                end = mid
            
        return end 
