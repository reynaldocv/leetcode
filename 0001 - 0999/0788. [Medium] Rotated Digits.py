# https://leetcode.com/problems/rotated-digits/

class Solution:
    def rotatedDigits(self, n: int) -> int:
        def product(A, B):
            ans = []
            for a in A:
                for b in B:
                    ans.append(a + b)
            return ans
        t = len(str(n))
     
        allpossible = [""]
        values = ["0", "1", "2", "5", "6", "8", "9"]
        values2 = "2569"
        for i in range(t):
            allpossible = product(allpossible, values)
        
        ans = 0
        for num in allpossible: 
            number = int(num)
            if number <= n:            
                go = False
                for l in num: 
                    if l in values2: 
                        go = True
                        break
                if go: 
                    ans += 1
        return ans
                    
