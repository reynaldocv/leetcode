# https://leetcode.com/problems/minimum-absolute-difference-queries/

class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        index = defaultdict(lambda: [])
        for (i, num) in enumerate(nums):
            index[num].append(i)
            
        keys = sorted(index)
        
        ans = []
        
        for (left, right) in queries: 
            prev, val = 0, inf
            for key in keys: 
                idx = bisect_left(index[key], left)
                if idx < len(index[key]) and index[key][idx] <= right: 
                    if prev: 
                        val = min(val, key - prev)
                    
                    prev = key
                    
            ans.append(val if val < inf else -1)
            
        return ans
                
            
