# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = (inf, inf)
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while k - j > 0:
                aux = nums[i] + nums[j] + nums[k]
                ans = min(ans, (abs(aux - target), aux))               
                if aux == target: 
                    return target
                elif aux < target:
                    j += 1
                else: 
                    k -= 1
        return ans[1]
        
