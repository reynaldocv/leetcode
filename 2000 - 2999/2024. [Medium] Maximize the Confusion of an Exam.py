# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

 def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def helper(val):
            stack = []
            start = -1
            ans = 0
            for i in range(n):
                if answerKey[i] == val:
                    stack.append(i)
                    if len(stack) <= k: 
                        ans = max(ans, i - start)
                    else: 
                        start = stack.pop(0)
                else: 
                    ans = max(ans, i - start)
            return ans
        
        n = len(answerKey)
        
        return max(helper("T"), helper("F"))
                    
        
