# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = defaultdict(lambda: 0)
        
        for char in chars: 
            counter[char] += 1
            
        ans = 0 
            
        for word in words: 
            n = len(word)
            
            cnt = defaultdict(lambda: 0)
            
            add = True
            
            for char in word:
                cnt[char] += 1 
                
                if cnt[char] > counter[char]:
                    add = False 
                    
                    break 
                
            if add: 
                ans += n 
                
        return ans 
                    
