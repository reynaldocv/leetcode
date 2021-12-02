# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = defaultdict(lambda: 0)
        
        for num in arr: 
            counter[num] += 1
        
        ans = len(counter)
        
        heap = []
        
        for key in counter:             
            heappush(heap, (counter[key], key))
            
        while heap and heap[0][0] <= k: 
            ans -= 1
            k -= heap[0][0]
            heappop(heap)
            
        return ans
