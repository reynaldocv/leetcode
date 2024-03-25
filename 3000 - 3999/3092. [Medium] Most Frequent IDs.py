# https://leetcode.com/problems/most-frequent-ids/

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        frequence = defaultdict(lambda: 0)
        
        heap = []
        
        ans = []
        
        for (i, num) in enumerate(nums):
            frequence[num] -= freq[i]
            
            heappush(heap, (frequence[num], num))
            
            while heap and heap[0][0] != frequence[heap[0][1]]:
                heappop(heap)
                
            if heap: 
                ans.append(-heap[0][0])
                
            else: 
                ans.append(0)
                
        return ans
        
