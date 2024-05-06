# https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        
        quo = n//k 
        
        counter = defaultdict(lambda: 0)
        
        maxElem = 0 
        
        for i in range(quo):
            tmp = word[i*k : (i + 1)*k]
            
            counter[tmp] += 1 
            
            maxElem = max(maxElem, counter[tmp])
            
        return quo - maxElem
        
