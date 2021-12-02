# https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        newChar = []
        
        last = ""
        counter = 0
        for char in chars + ["$$"]: 
            if char == last: 
                counter += 1
            else: 
                if counter > 0:                     
                    newChar.append(last)
                    if counter > 1:
                        newChar.extend([x for x in str(counter)])
                last = char
                counter = 1
                        
        for i in range(len(newChar)):
            chars[i] = newChar[i]
            
        chars = chars[:len(newChar)]
        
        return len(chars)
