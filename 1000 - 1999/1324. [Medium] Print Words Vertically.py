# https://leetcode.com/problems/print-words-vertically/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        
        m = max(len(word) for word in words)
        
        counter = defaultdict(lambda: 0)
        
        for word in words:
            for (ith, _) in enumerate(word):
                counter[ith] += 1
                
        letters = defaultdict(lambda: "")
        
        for word in words:
            for i in range(m):
                if counter[i] > 0:
                    if i < len(word):
                        counter[i] -= 1
                        
                        char = word[i]
                        
                    else:
                        char = " "
                
                else:
                    char = ""
                        
                letters[i] += char 
                
        return [letters[i] for i in range(m)]
    
        
        
                
        
