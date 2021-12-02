# https://leetcode.com/problems/largest-divisible-subset/

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = [[]]
        nums.sort()
        for num in nums:
            aux = []
            for s in dp: 
                if s and num % s[-1] == 0: 
                    aux.append(s + [num])
                else: 
                    aux.append([num])
            
            dp.append(max(aux, key = len))

        return max(dp, key=len)
