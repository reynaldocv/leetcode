# https://leetcode.com/problems/maximum-score-words-formed-by-letters/

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def helper(idx):
            if idx == n: 
                return 0 
            
            else: 
                ans = 0 
                
                for i in range(idx, n):
                    cnt = defaultdict(lambda: 0)
                    
                    for char in words[i]:
                        cnt[char] += 1 
                        
                    if all(cnt[char] <= counter[char] for char in cnt):
                        scr = 0 
                        
                        for char in cnt: 
                            counter[char] -= cnt[char]
                            
                            scr += score[index[char]]*cnt[char]
                            
                        ans = max(ans, scr + helper(i + 1))
                        
                        for char in cnt: 
                            counter[char] += cnt[char]
                
                return ans                     
                    
        index = {chr(ord("a") + i): i for i in range(26)}
        
        counter = defaultdict(lambda: 0)
        
        for letter in letters: 
            counter[letter] += 1 
            
        n = len(words)
        
        ans = helper(0)
        
        return ans 
            
        
            
        
