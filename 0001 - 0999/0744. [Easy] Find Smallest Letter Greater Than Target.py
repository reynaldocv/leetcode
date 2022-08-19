# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        
        start = -1
        end = n 
        
        while end - start > 1: 
            mid = (end + start)//2
            
            if letters[mid] <= target:
                start = mid 
            else:
                end = mid 
                
        return letters[0] if end == n else letters[end]
                
        
        
