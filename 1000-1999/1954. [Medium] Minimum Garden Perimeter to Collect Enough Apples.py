# https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/

class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        def somatoria(n):
            return n*(n + 1)//2
        
        apples = 0 
        i = 0
        while apples < neededApples:
            i += 1            
            apples += 4*(somatoria(2*i) - somatoria(i - 1))
            if i + 1 <= 2*i - 1:
                apples += 4*(somatoria(2*i - 1) - somatoria(i))
        
        return i*8
