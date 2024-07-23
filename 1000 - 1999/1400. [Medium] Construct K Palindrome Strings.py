# https://leetcode.com/problems/construct-k-palindrome-strings/

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        
        counter = defaultdict(lambda: 0)
        
        for char in s: 
            counter[char] += 1 
            
        odd = even = 0
            
        for key in counter: 
            if counter[key] % 2 == 0: 
                even += 1
            
            else: 
                odd += 1 
                
        if odd > k or k - odd > n - odd: 
            return False 
        
        return True
        
        
