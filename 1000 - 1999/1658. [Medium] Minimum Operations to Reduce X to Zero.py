# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        sumLeft, sumRight = 0, 0
        left, right = {0: 0}, {0: 0}
        for i in range(n): 
            sumLeft += nums[i]
            left[sumLeft] = left.get(sumLeft, i + 1)
            
            sumRight += nums[~i]
            right[sumRight] = right.get(sumRight, i + 1)
            
        ans = inf
        sumL = 0 
        sumR = sum(nums)
        if sumR == x: 
            return n
        
        for num in nums:
            sumL += num
            sumR -= num
            if sumL <= x: 
                if left[sumL] + right.get(x - sumL, inf) < n: 
                    ans = min(ans, left[sumL] + right.get(x - sumL, inf))
            if sumR <= x: 
                if left.get(x - sumR, inf) + right[sumR] < n: 
                    ans = min(ans, left.get(x - sumR, inf) + right[sumR])
            
        return ans if ans != inf else -1
