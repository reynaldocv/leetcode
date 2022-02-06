# https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:       
        k=len(nums)//3
        
        minHeap, maxHeap = [], []
        minLeft, maxRight = [], []
        
        minSum, maxSum = 0, 0
        
        for num in nums[:-k]:
            heappush(minHeap, -num)
            minSum += num
            if len(minHeap) > k: 
                minSum += heappop(minHeap)
            
            minLeft.append(minSum)
            
        for num in nums[::-1][:-k]:
            heappush(maxHeap,num)
            maxSum += num
            if len(maxHeap) > k: 
                maxSum -= heappop(maxHeap)
            
            maxRight.append(maxSum)
            
        minLeft = minLeft[k-1:]
        maxRight = maxRight[k-1:][::-1]
        
        ans = inf
        for i in range(k + 1):
            ans = min(ans, minLeft[i] - maxRight[i])
        
        return ans
        
