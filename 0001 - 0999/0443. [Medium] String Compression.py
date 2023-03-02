# https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = ""
        count = 1 
        
        ans = 0 
        
        lastChar = chars[-1]
        
        for char in chars + [chr(ord(lastChar) + 1)]:
            if prev != char: 
                if prev != "":
                    chars[ans] = prev
                    ans += 1
                    
                    if count > 1:                    
                        for digit in str(count):
                            chars[ans] = digit
                            ans += 1 
                        
                prev = char
                count = 1 
            
            else: 
                count += 1                 
        
        return ans
