# https://leetcode.com/problems/sum-of-k-mirror-numbers/

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        @cache
        def helper(start, qnt):
            if qnt == 1: 
                return [str(i) for i in range(start, k)]
            
            elif qnt == 2: 
                return [str(i) + str(i) for i in range(start, k)]
            
            else: 
                ans = []
                
                for elem in [str(i) for i in range(start, k)]:
                    for center in helper(0, qnt - 2):
                        newElem = elem + center + elem
                        
                        ans.append(newElem)
                        
                return ans
            
        digits = 1
        counter = 0
        
        ans = 0 
        
        while True:
            for num in helper(1, digits):
                numBase = str(int(num, k))
                
                if numBase == numBase[:: -1]:
                    counter += 1 
                    
                    ans += int(numBase)
                    
                    if counter == n: 
                        return ans 
                    
            digits += 1  
