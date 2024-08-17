# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        prev = nums[0] - 1
        cnt = 0 

        ans = []

        for num in nums: 
            if num == prev + 1: 
                cnt += 1 

            else: 
                cnt = 1 

            prev = num

            if cnt >= k: 
                ans.append(num)

            else: 
                ans.append(-1)

        return ans[k - 1: ]
