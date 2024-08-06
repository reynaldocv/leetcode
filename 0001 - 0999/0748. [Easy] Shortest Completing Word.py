# https://leetcode.com/problems/shortest-completing-word/
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        chars = [chr(ord("a") + i) for i in range(26)]
        
        counter = defaultdict(lambda: 0)
        
        for char in licensePlate: 
            minChar = char.lower()
            
            if minChar in chars: 
                counter[minChar] += 1 
            
        ans = (inf, inf, "")
        
        for (i, word) in enumerate(words): 
            count = defaultdict(lambda: 0)
            
            for char in word: 
                minChar = char.lower()
                
                if minChar in counter: 
                    count[minChar] += 1 
                    
            go = True 
            
            for key in counter: 
                if key not in count or counter[key] > count[key]:
                    go = False 
                    
                    break 
                    
            if go:
                ans = min(ans, (len(word), i,  word))
            
        return ans[2]
                
