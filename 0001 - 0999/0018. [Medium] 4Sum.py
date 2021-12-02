# https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4: 
            return []
        else: 
            nums.sort()
            ans = []
            exist = {}
            for i in range(n):
                for j in range(i + 1, n):
                    k = j + 1
                    l = n - 1
                    while l - k > 0:
                        aux = nums[i] + nums[j] + nums[k] + nums[l] 
                        if aux == target: 
                            key = str(nums[i]) + "-" + str(nums[j]) + "-" + str(nums[k]) + "-" + str(nums[l])
                            if key not in exist:  
                                ans.append([nums[i], nums[j], nums[k], nums[l]])
                                exist[key] = True                                
                        if aux > target: 
                            l -= 1
                        else: 
                            k += 1
            return ans
