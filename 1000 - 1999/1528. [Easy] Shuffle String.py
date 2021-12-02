# https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        aux = [(indices[i],s[i]) for i in range(len(indices))]
        aux.sort()
        ans = ""
        for (i, j) in aux:
            ans += j
        return ans
        
