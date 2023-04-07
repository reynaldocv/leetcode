# https://leetcode.com/problems/count-binary-substrings/

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        
        ans = 0 
        
        for (i, char) in enumerate(s):
            left = i 
            right = i + 1

            while 0 <= left and right < n and s[left] != s[right] and s[left] == s[i]:
                ans += 1 

                left -= 1
                right += 1 
        
        return ans 
    
class Solution2:
    def countBinarySubstrings(self, s: str) -> int:
        counter = []
        
        count = 1 
        last = s[0]
        
        for char in s[1: ] + "$": 
            if char != last: 
                counter.append(count)
                
                count = 1 
                last = char 
            
            else: 
                count += 1
                
        n = len(counter)
        
        ans = 0 
        
        for i in range(n - 1):
            ans += min(counter[i], counter[i + 1])
    
        return ans 
        
            
        
                    
