# https://leetcode.com/problems/maximum-product-of-three-numbers/

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        arrPos = []
        arrNeg = []
        arrPos.sort()
        for i in range(len(nums)):             
            arrPos.append(nums[i])
            if len(arrPos) >= 4:
                arrPos.sort()
                arrPos = arrPos[1:]
            if nums[i] < 0:
                arrNeg.append(nums[i])                
                if len(arrNeg) >= 3:
                    arrNeg.sort()
                    arrNeg.pop()
        ans, ans1, ans2 = 1, 0, 0
        if len(arrNeg) == 2:
            ans1 = arrNeg[0] * arrNeg[1] * arrPos[2]
        ans2 = arrPos[0] * arrPos[1] * arrPos[2]
        ans = max(ans1, ans2)
        return ans
            
