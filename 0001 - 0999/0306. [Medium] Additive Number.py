# https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def helper(prev, cur, s):
            if cur == s: 
                return True
            elif cur in s: 
                if s.index(cur) == 0:
                    newCur = int(cur) + int(prev)
                    return helper(cur, str(newCur), s[len(cur):])
                    
            return False
        
        n = len(num)
        for i in range(1, n - 1):
            for j in range(i + 1, n):                                
                num1 = num[:i]
                num2 = num[i: j]
                first = (num1 == "0" or (len(num2) > 0 and num1[0]!= "0"))
                second = (num2 == "0" or (len(num2) > 0 and num2[0]!= "0"))
                if first and second: 
                    if helper(num2, str(int(num1) + int(num2)), num[j:]):
                        return True

        return False
