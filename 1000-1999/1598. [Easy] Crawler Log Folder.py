# https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = []
        n = len(logs)
        for i in range(n):
            log = logs[i][0: len(logs[i]) - 1]
            if log == ".":
                continue
            elif log == "..":
                if len(ans) > 0:
                    ans.pop()
            else: 
                ans.append(log)
                
        return len(ans)
                
