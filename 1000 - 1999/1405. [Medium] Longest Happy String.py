# https://leetcode.com/problems/longest-happy-string/

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        
        for (char, cnt) in [("a", -a), ("b", -b), ("c", -c)]:
            if cnt != 0: 
                heappush(heap, (cnt, char))
            
        ans = ""
        
        prev = "$"
        counter = 1 
        
        while heap:             
            (cnt1, char1) = heappop(heap)
            
            if prev == char1 and counter == 2: 
                if heap: 
                    (cnt2, char2) = heappop(heap)
                    
                    prev = char2
                    ans += char2 
                    
                    counter = 1 
                    
                    if cnt2 != -1: 
                        heappush(heap, (cnt2 + 1, char2))
                    
                else: 
                    break 
                    
                heappush(heap, (cnt1, char1))
            
            else: 
                if prev == char1: 
                    counter += 1 
                    
                else: 
                    countner = 1 
                    
                prev = char1                
                ans += char1
                    
                if cnt1 != -1: 
                    heappush(heap, (cnt1 + 1, char1))
                
        return ans 
            
