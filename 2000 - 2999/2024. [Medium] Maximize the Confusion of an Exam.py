# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def helper(value):
            lastIndex = defaultdict(lambda: -1)
            lastIndex[0] = -1 
            
            ans = cnt = 0 
            
            for (i, char) in enumerate(answerKey): 
                if char == value: 
                    cnt += 1 
                    
                ans = max(ans, i - lastIndex[cnt - k])
                
                if cnt not in lastIndex: 
                    lastIndex[cnt] = i 
                    
            return ans
        
        return max(helper("F"), helper("T"))
                    
        
