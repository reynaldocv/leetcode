# https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        ans = []
        for i in range(m):
            arr = nums[l[i]:r[i] + 1]
            arr.sort()
            ratio = arr[1] - arr[0]
            isArithmetic = True
            for j in range(2, len(arr)):
                if ratio != arr[j] - arr[j - 1]:
                    isArithmetic = False
                    break
            
            ans.append(isArithmetic)
        
        return ans
        
        
