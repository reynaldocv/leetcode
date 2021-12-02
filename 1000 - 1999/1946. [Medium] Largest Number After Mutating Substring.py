# https://leetcode.com/problems/largest-number-after-mutating-substring/

class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        change = change[:10]
        n = len(num)
        go = {1:0}
        ans = ""
        for i in range(n):
            if int(num[i]) < change[int(num[i])]:
                if go[1] == 0: 
                    go[1] = 1
                if go[1] == 1:
                    ans += str(change[int(num[i])])
                else: 
                    ans += num[i]    
            elif int(num[i]) == change[int(num[i])]:
                ans += str(change[int(num[i])])
                    
            elif go[1] == 0: 
                ans += num[i]
            elif go[1] == 1:
                go[1] = 2
                ans += num[i]
            else:
                ans += num[i]
