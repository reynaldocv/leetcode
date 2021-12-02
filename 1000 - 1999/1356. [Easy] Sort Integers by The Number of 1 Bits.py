# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def numberbits1(n):
            if n <= 0: return 0
            ans = 0
            while n > 0: 
                if n % 2 == 1:
                    ans += 1                    
                n = n//2
            return ans
        
        aux, n, ans = [], len(arr),  []
        for i in range(n):
            aux.append((numberbits1(arr[i]), arr[i]))
        
        aux.sort()
        
        for i in range(n):
            ans.append(aux[i][1])
            
        return ans
