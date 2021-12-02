# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = {}
        for i in t: 
            dic[i] = dic.get(i, 0) + 1
        for i in s:
            dic[i] = dic.get(i, 0) - 1
            if dic[i] == 0:
                del dic[i]
        
        ans = [*dic] 
        return ans[0]
            
