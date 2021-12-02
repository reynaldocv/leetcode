# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        exist = {}
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            j = i + 1
            k = n - 1
            while k - j > 0:
                sum3 = nums[i] + nums[j] + nums[k]
                if sum3 > 0: 
                    k -= 1
                elif sum3 < 0: 
                    j += 1
                else: 
                    key = str(nums[i]) + str(nums[j]) + str(nums[k])
                    if exist.get(key, False) == False:
                        ans.append([nums[i], nums[j], nums[k]])
                        exist[key] = True
                    j += 1
            
        return ans
                    
