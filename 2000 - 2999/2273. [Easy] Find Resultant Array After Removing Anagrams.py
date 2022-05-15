# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words) 
        
        start = 0 
        ans = []
        
        while start < n:
            k = 1
            key = sorted(words[start])
            while start + k < n and sorted(words[start + k]) == key:
                k += 1
                
            k -= 1 
            
            ans.append(words[start])
            
            start += k + 1
            
        return ans
        
