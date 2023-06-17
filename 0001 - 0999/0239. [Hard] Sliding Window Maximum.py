# https://leetcode.com/problems/sliding-window-maximum/submissions/

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        heap = []
        for i in range(k):
            heappush(heap, (-nums[i], i))
        
        ans = [-heap[0][0]]
        
        for i in range(k, n):
            heappush(heap, (-nums[i], i))
            
            while heap[0][1] <= i - k:
                heappop(heap)
            
            ans.append(-heap[0][0])
            
        return ans
            
class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr = []
        
        for num in nums[: k - 1]:
            arr.append(num) 
            
        arr.sort() 
        
        ans = []
        
        for (i, num) in enumerate(nums[k - 1: ]):
            insort(arr, num)
            
            ans.append(arr[-1])
            
            idx = bisect_left(arr, nums[i])
            
            arr.pop(idx)
            
        return ans 
            
        
        
        
