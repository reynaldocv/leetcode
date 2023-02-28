# https://leetcode.com/problems/most-common-word/

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = {word.lower() for word in banned}
        
        chars = {chr(ord("a") + i) for i in range(26)}
        
        counter = defaultdict(lambda: 0)
        
        ans = (0, "")
        
        word = ""
        
        for char in paragraph + " ":
            minChar = char.lower()
            
            if minChar in chars:
                word += minChar
                
            elif word != "":                
                if word not in banned:             
                    counter[word] += 1                
                    ans = max(ans, (counter[word], word))
                
                word = ""
        
        return ans[1]
                
