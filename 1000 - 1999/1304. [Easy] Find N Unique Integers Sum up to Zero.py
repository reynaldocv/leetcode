# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 1:
            ans = [x for x in range(-n//2 + 1, n//2 + 1)]
        else:
            if n == 0: return []
            m = n + 1
            ans = [x for x in range(-m//2 + 1, m//2 + 1)]
            aux = ans.pop()
            aux += ans.pop()
            ans.append(aux)
            
                
        return ans
