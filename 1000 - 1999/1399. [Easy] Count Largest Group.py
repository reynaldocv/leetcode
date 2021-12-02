# https://leetcode.com/problems/count-largest-group/

class Solution:
    def countLargestGroup(self, n: int) -> int:
        def SumOfDigits(n):
            if n <= 0: return 0
            return n % 10 + SumOfDigits(n//10) 
        
        max_ = 0
        sumDigDic = {}
        for i in range(1, n + 1):
            aux = SumOfDigits(i)
            sumDigDic[aux] = sumDigDic.get(aux, 0) + 1
            max_ = max(max_, sumDigDic[aux])
        ans = 0
        for i in sumDigDic:
            if sumDigDic[i] == max_:
                ans += 1
        return ans
            
