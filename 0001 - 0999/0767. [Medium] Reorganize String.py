# https://leetcode.com/problems/reorganize-string/

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = defaultdict(lambda: 0)
        heap = []
        for char in s:
            counter[char] += 1
            
        for key in counter: 
            heappush(heap, (-counter[key], key))
            
        ans = "$"
        while heap: 
            if ans[-1] != heap[0][1]:
                (k, char) = heappop(heap)
                ans += char
                k += 1
                if k != 0: 
                    heappush(heap, (k, char))
                    
            elif len(heap) >= 2:
                (k1, char1) = heappop(heap)
                (k2, char2) = heappop(heap)
                ans += char2
                k2 += 1
                if k2 != 0: 
                    heappush(heap, (k2, char2))
                heappush(heap, (k1, char1))
            
            else:
                break
                
        ans = ans[1:]
        
        return ans if len(ans) == len(s) else ""
        
