# https://leetcode.com/problems/longest-uncommon-subsequence-ii/

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubsequence(subWord, word):
            i, j = 0, 0
            n, m = len(word), len(subWord)
            while i < m and j < n: 
                if subWord[i] == word[j]:
                    i += 1
                j += 1
            return True if i == m else False
        
        counter = {s: strs.count(s) for s in strs}
        uniqueStrs = [*counter]
        uniqueStrs.sort(reverse = True, key = lambda item: len(item))
        seen = {}
        
        for word in uniqueStrs: 
            if counter[word] == 1:
                if not any ([isSubsequence(word, subWord) for subWord in seen]):
                    return len(word)
            else: 
                seen[word] = True
        
        return -1
        
