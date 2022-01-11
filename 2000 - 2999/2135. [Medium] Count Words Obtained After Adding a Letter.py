# https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        seen = defaultdict(lambda: 0)
        for word in targetWords:
            seen["".join(sorted(word))] += 1
            
        added = {}
        ans = 0
        for word in startWords: 
            chars = {}
            for char in word: 
                chars[char] = True
                
            for i in range(26):
                char = chr(i + ord("a"))
                if char not in chars: 
                    aux = "".join(sorted(word + char))
                    if aux in seen and aux not in added: 
                        added[aux] = True
                        ans += seen[aux]
                  
        return ans
            
