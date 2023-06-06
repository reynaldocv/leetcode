# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        arr = [0]
        seen = set()
        
        for num in nums: 
            if num > 0 and num not in seen: 
                seen.add(num)
                
                arr.append(num)
                
        arr.sort()
                
        n = len(arr)
            
        start = 0         
        end = n
        
        while end - start > 1: 
            middle = (end + start)//2
            
            if arr[middle] == middle: 
                start = middle 
                
            else: 
                end = middle 
                
        return end 
        
        
