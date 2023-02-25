# https://leetcode.com/problems/find-lucky-integer-in-an-array/

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = defaultdict(lambda: 0)
        
        for num in arr: 
            counter[num] += 1 
            
        ans = -1
        
        for key in counter: 
            if key == counter[key]:
                ans = max(ans, key)
                
        return ans 
