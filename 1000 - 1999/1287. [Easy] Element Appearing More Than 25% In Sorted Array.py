# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        
        counter = defaultdict(lambda: 0)
        
        for num in arr: 
            counter[num] +=1 
            
            if counter[num]*4 > n:
                return num 
            
        
                
