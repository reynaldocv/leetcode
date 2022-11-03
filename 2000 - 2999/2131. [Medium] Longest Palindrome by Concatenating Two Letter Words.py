# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = defaultdict(lambda: 0)
        
        for word in words: 
            counter[word] += 1 
            
        ans = 0 
        middle = False 
        
        for key in counter: 
            reversedKey = key[:: -1]
            
            if key != reversedKey:
                if reversedKey in counter: 
                    value = min(counter[key], counter[reversedKey])
                    ans += value*4 

                    counter[key] -= value
                    counter[reversedKey] -= value

            else: 
                ans += (counter[key]//2)*4
                
                if counter[key] % 2 == 1: 
                    middle = True 
                    
        return ans + 2 if middle else ans
                
                
            
