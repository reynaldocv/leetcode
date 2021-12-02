# https://leetcode.com/problems/increasing-decreasing-string/

class Solution:
    def sortString(self, s: str) -> str:
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        
        ans = "";
        while len(dic) > 0:
            for a in sorted(dic.keys()):
                ans += a
                dic[a] -= 1
                if dic[a] == 0:
                    del dic[a]
            for a in sorted(dic.keys(), reverse = True):
                ans += a
                dic[a] -= 1
                if dic[a] == 0:
                    del dic[a]
        return ans
            
            
