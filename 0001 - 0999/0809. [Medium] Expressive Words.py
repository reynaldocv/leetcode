# https://leetcode.com/problems/expressive-words/

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def helper(word):
            ans = []
            prefix = ""
            cnt = 0 
            for char in word + "$": 
                if prefix != char: 
                    if prefix != "":
                        ans.append((prefix, cnt))
                    prefix = char
                    cnt = 1 
                else: 
                    cnt += 1 
                    
            return ans 
        
        def collaborator(word):
            cnt = helper(word)
            if len(counter) != len(cnt):
                return False 
            else: 
                for ((char1, q1), (char2, q2)) in zip(counter, cnt):
                    if char1 != char2 or q2 > q1: 
                        return False
                    if q1 == q2: 
                        continue
                    if q1 < 3: 
                        return False 
                
                return True 
            
        counter = helper(s)
        ans = 0 
        for word in words: 
            if collaborator(word):
                ans += 1 
                
        return ans
                
    
                
                        
        
