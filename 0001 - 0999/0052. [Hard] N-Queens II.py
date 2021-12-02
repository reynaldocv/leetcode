# https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        def countWays(n, i):
            ans = 0 
            for j in range(n):
                if j not in set1 and j - i not in set2 and j + i not in set3: 
                    if n - 1 == i: 
                        return 1
                    set1.add(j)
                    set2.add(j - i)
                    set3.add(j + i)                    
                    ans += countWays(n, i + 1)
                    set1.discard(j)
                    set2.discard(j - i)
                    set3.discard(j + i)  
            
            return ans
                
        set1, set2, set3 = set(), set(), set()
        return countWays(n, 0)
                
                        
