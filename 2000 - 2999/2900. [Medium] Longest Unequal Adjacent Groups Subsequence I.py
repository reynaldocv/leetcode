# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        prev = groups[0]
        ans = [words[0]]
        
        for i in range(1, n):
            if prev != groups[i]:
                prev = groups[i]
                
                ans.append(words[i])
                
        return ans 
            
