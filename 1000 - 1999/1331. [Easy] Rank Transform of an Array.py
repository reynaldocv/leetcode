# https://leetcode.com/problems/rank-transform-of-an-array/

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        tmp = [num for num in arr]
        
        tmp.sort()
        
        index = defaultdict(lambda: 0)
        
        i = 1 
        
        for num in tmp: 
            if index[num] == 0: 
                index[num] = i 
                
                i += 1 
                
        ans = []
        
        for num in arr: 
            ans.append(index[num])
            
        return ans 
        
        
