# https://leetcode.com/problems/longest-uncommon-subsequence-ii/

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def helper(subWord, word):
            n, m = len(word), len(subWord)
            
            i, j = 0, 0
            
            while i < m and j < n: 
                if subWord[i] == word[j]:
                    i += 1
            
                j += 1
            
            return i == m 
        
        counter = defaultdict(lambda: 0) 
        
        for word in strs: 
            counter[word] += 1 
        
        uniqueStrs = [key for key in counter]
        
        uniqueStrs.sort(key = lambda item: -len(item))
        
        seen = {}
        
        for word in uniqueStrs: 
            if counter[word] == 1:
                if not any ([helper(word, subWord) for subWord in seen]):
                    return len(word)
                
            else: 
                seen[word] = True
        
        return -1
