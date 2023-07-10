# https://leetcode.com/problems/substring-with-largest-variance/

class Solution:
    def largestVariance(self, s: str) -> int:
        def helper(a, b):
            ans = prev = 0
            
            seen = set()
           
            cntA = counter[a]
            cntB = counter[b]
            
            for char in s:			
                if char != a and char != b:
                    continue

                if prev < 0 and cntA != 0 and cntB != 0:
                    prev = 0
                    
                    seen = set() 
                    
                if char == a:
                    prev += 1
                    cntA -= 1
                    
                    seen.add(a)
                    
                if char == b:
                    prev -= 1
                    cntB -=1
                    
                    seen.add(b)
                    
                if len(seen) == 2:
                    ans = max(ans, prev)
                    
            return ans
            
        counter = defaultdict(lambda: 0)
        
        for char in s: 
            counter[char] += 1 

        ans = 0 
        
        for (a, b) in permutations(counter, 2):
            ans = max(ans, helper(a, b))
            
        return ans         
