# https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        counter = [0]
        
        prev = 0 
        
        for word in words:
            if word[0] in "aeiou" and word[-1] in "aeiou":
                prev += 1 
                
            counter.append(prev)
            
        ans = []
        
        for (start, end) in queries:
            ans.append(counter[end + 1] - counter[start])
            
        return ans 
        
        
