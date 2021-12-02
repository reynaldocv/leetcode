# https://leetcode.com/problems/number-of-equivalent-domino-pairs/

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        def Combination(a, b):
            ans = 1
            c = max(a - b, b)
            d = min(a - b, b)
            for i in range(a, c ,  - 1):
                ans *= i
            for i in range(2, d + 1):
                ans //= i
            return ans
            
        dic = {}
        for domino in dominoes: 
            domino.sort()
            aux = domino[0]*10  + domino[1]
            dic[aux] = dic.get(aux, 0) + 1
        print(dic)
        ans = 0
        for k in dic: 
            if dic[k] > 1: 
                ans += Combination(dic[k], 2)
        
        return ans
