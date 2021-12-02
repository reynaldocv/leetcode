# https://leetcode.com/problems/buddy-strings/

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        dic = {}
        dif = 0
        pos = []
        n = len(s)
        if n != len(goal): return False
        for i in range(n):
            dic[s[i]] = dic.get(s[i], 0) + 1
            if s[i] != goal[i]:
                dif += 1
                pos.append(i)
        if dif != 2 and dif != 0: 
            return False
        elif dif == 2:
            if s[pos[0]] == goal[pos[1]] and s[pos[1]] == goal[pos[0]]:
                return True
            else: 
                return False
        else: 
            for k in dic: 
                if dic[k] >= 2:
                    return True
            return False
            
        
