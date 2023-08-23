# https://leetcode.com/problems/reorganize-string/

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = defaultdict(lambda: 0)
        
        for char in s: 
            counter[char] -= 1 
            
        heap = []
        
        for key in counter: 
            heappush(heap, (counter[key], key))
            
        prev = "$"        
        ans = ""
        
        while heap: 
            if heap[0][1] != prev: 
                (cnt, char) = heappop(heap)
                
                ans += char 
                prev = char
       
                if cnt < -1: 
                    heappush(heap, (cnt + 1, char))
                
            elif len(heap) >= 2: 
                (cnt1, char1) = heappop(heap)
                (cnt2, char2) = heappop(heap)
                
                heappush(heap, (cnt1, char1))
                
                ans += char2 
                prev = char2
                
                if cnt2 < -1: 
                    heappush(heap, (cnt2 + 1, char2))
                
            else: 
                return ""
            
        return ans
        
