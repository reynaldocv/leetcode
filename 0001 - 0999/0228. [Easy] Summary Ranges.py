# https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = None 
        prev = -inf 
        
        ans = []
        
        for num in nums + [inf]: 
            if prev + 1 == num:
                prev = num 
                
            else:
                if start != None: 
                    if start == prev: 
                        ans.append(str(start))
                    
                    else:                         
                        ans.append(str(start) + "->" + str(prev))
                
                start = num 
                prev = num 
                
        return ans 
                

