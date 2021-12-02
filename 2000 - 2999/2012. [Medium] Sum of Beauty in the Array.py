# https://leetcode.com/problems/sum-of-beauty-in-the-array/

    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        minimum = [num for num in nums]
        maximum = [num for num in nums]
        
        for i in range(1, n):
            maximum[i] = max(maximum[i], maximum[i - 1])
            
        for i in range(n - 2, -1,-1):
            minimum[i] = min(minimum[i], minimum[i + 1])
        
        ans = 0 
       
        for i in range(1, n - 1):
            if maximum[i - 1] < nums[i] < minimum[i + 1]:
                ans += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                ans += 1
        
        return ans
