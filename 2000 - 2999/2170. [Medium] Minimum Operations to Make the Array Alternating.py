# https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cntEven = defaultdict(lambda: 0)
        cntOdd = defaultdict(lambda: 0)
        
        n = len(nums)
        
        maxEven = (0, -1)
        maxOdd = (0, -1)
        
        for i in range(n):
            num = nums[i]
            if i % 2 == 0:
                cntEven[num] += 1 
                maxEven = max(maxEven, (cntEven[num], num))
            else: 
                cntOdd[nums[i]] += 1 
                maxOdd = max(maxOdd, (cntOdd[num], num))
        
        ans = inf
        if maxOdd[1] != maxEven[1]:
            ans = n - maxEven[0] - maxOdd[0]
        else: 
            cntEven[inf] = 0             
            for key in cntEven: 
                if key != maxEven[1]:
                    ans = min(ans, n - cntEven[key] - maxOdd[0])
            
            cntOdd[-inf] = 0 
            for key in cntOdd: 
                if key != maxOdd[1]:
                    ans = min(ans, n - cntOdd[key] - maxEven[0])
                    
        return ans
