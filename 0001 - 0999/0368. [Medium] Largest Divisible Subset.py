# https://leetcode.com/problems/largest-divisible-subset/

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = [[]]

        nums.sort() 
        
        for num in nums: 
            aux = []
            
            for arr in dp: 
                if arr and num % arr[-1] == 0: 
                    aux.append(arr + [num])
                    
                else: 
                    aux.append([num])
                    
            dp.append(max(aux, key = lambda item: len(item)))
            
        return max(dp, key = lambda item: len(item))
