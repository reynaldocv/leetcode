# https://leetcode.com/problems/split-strings-by-separator/

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        
        for word in words: 
            prev = ""
            
            for char in word + separator: 
                if char == separator: 
                    if prev != "":
                        ans.append(prev)
                        
                        prev = ""
                        
                else: 
                    prev += char
                    
        return ans 
