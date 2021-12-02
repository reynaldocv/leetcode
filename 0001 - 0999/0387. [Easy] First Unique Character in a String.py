# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        pos, dic = {}, {}
        n = len(s)
        for i in range(n):
            dic[s[i]] = dic.get(s[i], 0) + 1
            if s[i] not in pos: 
                pos[s[i]] = i
        ans = n
        print(dic)
        print(pos)
        for i in dic:
            if dic[i] == 1:
                ans = min(ans, pos[i])
        return -1 if ans == n else ans
            
        
        
        
