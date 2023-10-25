# https://leetcode.com/problems/distant-barcodes/

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)
        
        counter = defaultdict(lambda: 0)
        
        for num in barcodes: 
            counter[num] += 1 
            
        barcodes.sort(key = lambda item: (-counter[item], item))
        
        ans = [0 for _ in range(n)]
        
        idx = 0 
        
        for num in barcodes: 
            ans[idx] = num
            
            idx += 2 
            
            if idx >= n: 
                idx = 1 
                
        return ans 
        
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = defaultdict(lambda: 0)
        for barcode in barcodes:
            counter[barcode] += 1
            
        heap = []
        for key in counter: 
            heappush(heap, (-counter[key], key))
            
        ans = [inf]
        
        while heap: 
            same = False
            if heap[0][1] == ans[-1]:
                same = True
                (cnt, key) = heappop(heap)
            
            (cnt2, key2) = heappop(heap)
            ans.append(key2)
            cnt2 += 1
            if cnt2 != 0:
                heappush(heap, (cnt2, key2))
            
            if same: 
                heappush(heap, (cnt, key))
                
        return ans[1: ]
                
            
