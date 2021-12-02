# https://leetcode.com/problems/sum-of-k-mirror-numbers/

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        @cache 
        def helper(start, n):            
            if n == 1:
                return [str(i) for i in range(start, k)]
            if n == 2: 
                return [str(i) + str(i) for i in range(start, k)]
            else: 
                arr = []
                for elem in [str(i) for i in range(start, k)]:
                    for center in helper(0, n - 2):
                        arr.append(elem + center + elem[::-1])

                return arr
            
        digits = 1
        counter = 0
        ans = 0 
        while True:
            for num in helper(1, digits):
                numBase = str(int(num, k))
                if numBase == numBase[::-1]:
                    ans += int(numBase)
                    counter += 1
                    if counter == n: 
                        return ans
                
            digits += 1  
