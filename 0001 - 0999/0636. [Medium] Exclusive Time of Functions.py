# https://leetcode.com/problems/exclusive-time-of-functions/

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        def helper(string):
            tmp = string.split(":")
            return [int(tmp[0]), tmp[1], int(tmp[2])]
        
        m = len(logs)
        arr = []
        for i in range(m):
            arr.append(helper(logs[i]))
            
        stack = []
        ans = [0 for _ in range(n)]
        
        for (idx, process, time) in arr: 
            if process == "start":
                stack.append((idx, time))
            else: 
                (_, last) = stack.pop()
                executionTime = time - last + 1
                ans[idx] += executionTime
                if stack: 
                    ans[stack[-1][0]] -= executionTime
                    
        return ans
        
