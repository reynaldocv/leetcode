# https://leetcode.com/problems/sort-integers-by-the-power-value/

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def recursive(num):
            if num in seen: 
                return seen[num]
            else:
                ans = 0
                if num % 2 == 1: 
                    ans = 1 + recursive(num*3 + 1)                    
                else: 
                    ans = 1 + recursive(num // 2)
                seen[num] = ans
                return ans
            
        seen = {1: 1} 
        arr = []
        for num in range(lo, hi + 1):
            arr.append((recursive(num), num))
        
        arr.sort()
        
        return arr[k - 1][1]
        
