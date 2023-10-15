# https://leetcode.com/problems/last-visited-integers/

class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        ans = []
        
        prev = -1
        stack = []
        
        for word in words: 
            if word == "prev":                           
                if prev*-1 <= len(stack):
                    ans.append(stack[prev])
                    
                else: 
                    ans.append(-1)
                    
                prev -= 1 
                    
            else: 
                stack.append(int(word))
                
                prev = -1 
                
        return ans
