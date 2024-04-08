# https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/

class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        value = {chr(ord("a") + i): i for i in range(26)}
        
        ans = ""
        
        for char in s: 
            if k > 0: 
                print(char, k)
                
                distance = min(value[char], (-value[char]) % 26)
            
                if k >= distance: 
                    ans += "a"

                    k -= distance
                    
                else: 
                    minValue = min((value[char] + k) % 26, (value[char] - k) % 26)
                                        
                    ans += chr(ord("a") + minValue)
                    
                    k = 0 

            else: 
                ans += char
                
        return ans 
        
