# https://leetcode.com/problems/take-gifts-from-the-richest-pile/

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        n = len(gifts) 
        
        heap = []
        
        for (i, gift) in enumerate(gifts):
            heappush(heap, (-gift, i))
            
        for i in range(k):
            (gift, idx) = heappop(heap)
            
            if gift == -1: 
                break 
            
            newGift = int((-gift)**.5)
            
            gifts[idx] = newGift
            
            heappush(heap, (-newGift, idx))
            
        return sum(gifts)
            
