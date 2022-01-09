# https://leetcode.com/problems/word-subsets/

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def helper(word):
            ans = [0 for _ in range(26)]
            for letter in word: 
                ans[ord(letter) - ord("a")] += 1
                
            return ans
        
        bmax = [0 for _ in range(26)]
        for word in words2:
            for (i, cnt) in enumerate(helper(word)):
                bmax[i] = max(bmax[i], cnt)
                
        ans = []
        for word in words1:
            accepted = True
            for (i, cnt) in enumerate(helper(word)):
                if bmax[i] > cnt: 
                    accepted = False
                    break
                    
            if accepted: 
                ans.append(word)
                
        return ans
                        
        
