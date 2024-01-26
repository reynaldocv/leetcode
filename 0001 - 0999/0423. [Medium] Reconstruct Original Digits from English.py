# https://leetcode.com/problems/reconstruct-original-digits-from-english/

class Solution:
    def originalDigits(self, s: str) -> str:
        oneLetter = ["zero", "wot", "urfo", "xsi", "ghtei"]
        twoLetters = ["oen", "three", "fvie", "sveen", "einn"]
        
        numbers = {"z": "0", "w": "2", "u": "4", "x": "6", "g": "8", "oe": "1", "th": "3", "fv": "5", "sv": "7", "ei": "9"}
        
        counter = defaultdict(lambda: 0)
        
        for char in s: 
            counter[char] += 1 
            
        ans = "" 
        
        for word in oneLetter: 
            first = word[0]    
             
            if first in counter:
                cnt = counter[first]
            
                for char in word: 
                    counter[char] -= cnt 
                    
                    if counter[char] == 0: 
                        counter.pop(char)
                        
                ans += numbers[first]*cnt
            
        for word in twoLetters: 
            first = word[0]            
            second = word[1]
            
            if first in counter and second in counter:
                cnt1 = counter[first]
                cnt2 = counter[second]
                
                cnt = min(cnt1, cnt2)
            
                for char in word: 
                    counter[char] -= cnt 
                    
                    if counter[char] == 0: 
                        counter.pop(char)
                        
                ans += numbers[first + second]*cnt
                
        return "".join(sorted(ans))
                    
        
        
                
        
