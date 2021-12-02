# https://leetcode.com/problems/greatest-sum-divisible-by-three/

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        div = [[],[],[]]
        totalSum = 0
        for num in nums: 
            totalSum += num
            res = num % 3
            if res > 0: 
                div[res].append(num)
                div[res].sort()
                div[res] = div[res][:2]
        
        res = totalSum % 3
        if res == 0: 
            return totalSum
        else:
            print(totalSum, div)
            res1 = div[res][0] if len(div[res]) > 0 else totalSum
            res2 = sum(div[3 - res]) if len(div[3 - res]) > 1 else totalSum
            return max(totalSum - res1, totalSum - res2)
            
