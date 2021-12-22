# https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def helper(word):
            for i in range(0, 26):
                char = chr(ord("a") + i)
                if char in word: 
                    return word.count(char)
            
        arr = []
        for word in words: 
            insort(arr, helper(word))
        
        n = len(arr)
        ans = []
        
        for query in queries:
            idx = bisect_right(arr, helper(query))
            ans.append(n - idx)
            
        return ans
        
            
        
