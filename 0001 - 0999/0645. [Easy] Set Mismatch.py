# https://leetcode.com/problems/set-mismatch/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0 for i in range(n + 1)]
        for num in nums:
            arr[num] += 1
        ans = [0, 0]
        for i in range(1, n + 1):
            if arr[i] == 2:
                ans[0] = i
            if arr[i] == 0:
                ans[1] = i    
        return ans
        
