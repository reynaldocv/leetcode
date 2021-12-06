# https://leetcode.com/problems/number-of-squareful-arrays/

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        @cache
        def isSquare(num):
            return (int(num**.5))**2 == num
        
        def helper(cnt, preNum):
            nonlocal ans
            if cnt == n:                 
                ans += 1
            else: 
                for num in counter:
                    if counter[num] > 0:
                        if isSquare(preNum + num):
                            counter[num] -= 1
                            helper(cnt + 1, num)
                            counter[num] += 1
                            
        n = len(nums)
        ans = 0 
        counter = defaultdict(lambda: 0)
        for num in nums: 
            counter[num] += 1

        for num in counter:
            counter[num] -= 1
            helper(1, num)
            counter[num] += 1

        return ans
