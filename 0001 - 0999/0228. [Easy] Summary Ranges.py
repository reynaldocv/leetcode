# https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        prev = -inf
        start = -inf 
        ans = []
        
        for num in nums + [inf]: 
            if prev + 1 != num: 
                if prev != -inf:
                    if start != prev: 
                        ans.append(str(start) + "->" + str(prev))
                    else:
                        ans.append(str(start))
                
                start = num 
                prev = num 
            
            else: 
                prev = num 
                
        return ans 
                

