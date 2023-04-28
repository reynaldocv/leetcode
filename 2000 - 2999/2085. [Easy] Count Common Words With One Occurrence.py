# https://leetcode.com/problems/count-common-words-with-one-occurrence/

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter = defaultdict(lambda: [0, 0])
        
        for (i, words) in enumerate([words1, words2]):
            for word in words: 
                counter[word][i] += 1 
                
        ans = 0     
            
        for key in counter: 
            if counter[key] == [1, 1]:
                ans += 1 
        
        return ans 
