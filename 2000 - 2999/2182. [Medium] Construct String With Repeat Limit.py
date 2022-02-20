# https://leetcode.com/problems/construct-string-with-repeat-limit/

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = defaultdict(lambda: 0)
        for char in s: 
            counter[char] += 1 
            
        heap = []
        for key in counter: 
            heappush(heap, (-ord(key), counter[key]))
            
        ans = []
        cnt = 0 
        
        while heap: 
            (ascci, q) = heappop(heap)
            if ans and ans[-1] == ascci and cnt == repeatLimit: 
                if not heap: 
                    break
                (ascci2, q2) = heappop(heap)
                ans.append(ascci2)
                cnt = 1 
                if q2 - 1:
                    heappush(heap, (ascci2, q2 - 1))
                
                heappush(heap, (ascci, q))                
            else: 
                if not ans or ans[-1] != ascci: 
                    cnt = 0
                
                cnt += 1 
                ans.append(ascci)
                if q - 1: 
                    heappush(heap, (ascci, q - 1))
                    
        return "".join(chr(-x) for x in ans)
    
