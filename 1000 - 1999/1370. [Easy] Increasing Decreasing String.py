# https://leetcode.com/problems/increasing-decreasing-string/

class Solution:
    def sortString(self, s: str) -> str:
        n = len(s)
        
        counter = defaultdict(lambda: 0)
        letters = set() 
        
        for char in s: 
            counter[char] += 1             
            letters.add(char)
            
        letters = [elem for elem in letters]
        
        letters.sort() 
                
        ans = ""
        
        while len(ans) < n:           
            for letter in letters: 
                if counter[letter] > 0: 
                    ans += letter
                
                counter[letter] -= 1 
            
            for letter in letters[:: -1]: 
                if counter[letter] > 0: 
                    ans += letter
                
                counter[letter] -= 1 
                
        return ans 
            
