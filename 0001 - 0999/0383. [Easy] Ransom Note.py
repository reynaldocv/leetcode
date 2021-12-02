# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic1, dic2, ans = {}, {}, True
        for i in magazine: 
            dic1[i] = dic1.get(i, 0) + 1
        for i in ransomNote: 
            if i in dic1: 
                dic2[i] = dic2.get(i, 0) + 1
                if dic2[i] > dic1[i]:
                    ans = False
                    break
            else:
                ans = False
                break
        return ans
        
