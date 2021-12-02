# https://leetcode.com/problems/expression-add-operators/

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def backtrack(i, prev, curr, total = 0, path = []):
            if i == len(num):
                if total == target and curr == 0:
                    ans.append("".join(path[1:]))
            else:
                curr = curr * 10 + int(num[i])
                if curr > 0:
                    backtrack(i + 1, prev, curr, total, path)
                backtrack(i + 1, curr, 0, total + curr, path + ["+", str(curr)])
                if path:
                    backtrack(i + 1, -curr, 0, total - curr, path + ["-", str(curr)])
                    backtrack(i + 1, curr*prev, 0, total - prev + (prev * curr), path + ["*", str(curr)])

        ans = []
        backtrack(0, 0, 0, 0, [])
        return ans

class Solution2: #(Time Limit Exceeded)
    def addOperators(self, num: str, target: int) -> List[str]:
        def hasLeadingZeros(s):
            ans = ""
            num = 0 
            for char in s: 
                if char.isdigit():
                    num = (num * 10) + int(char)
                else: 
                    ans += str(num) + char
                    num = 0
            ans = ans + str(num)
            return ans == s
        
        def helper(oldS, i):
            if i == n - 1: 
                oldS += num[i]                
                if hasLeadingZeros(oldS) and eval(oldS) == target: 
                    ans.append(oldS)
            else: 
                helper(oldS + num[i] + "+", i + 1)
                helper(oldS + num[i] + "-", i + 1)
                helper(oldS + num[i] + "*", i + 1)

                helper(oldS + num[i], i + 1)

        ans = []
        n = len(num)
        helper("", 0)
        
        return ans
