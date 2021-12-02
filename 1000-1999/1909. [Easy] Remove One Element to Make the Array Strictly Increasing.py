# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)
        inc = [False for i in range(n)]
        dec = [False for i in range(n)]
        inc[0] = True
        dec[n -1] = True
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                inc[i] = True
            else:
                break
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                dec[i] = True
            else:
                break
             
        print(inc)
        print(dec)
        ans = inc[n - 2] or dec[1]
        
        if ans: 
            return ans
        
        for i in range(1, n - 1):
            if inc[i - 1] == True and dec[i + 1] == True:
                if nums[i - 1] < nums[i + 1]:
                    return True
        
        
    
