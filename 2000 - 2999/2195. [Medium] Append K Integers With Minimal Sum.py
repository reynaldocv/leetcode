# https://leetcode.com/problems/append-k-integers-with-minimal-sum/

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        seen = {}
        nums.sort()
        
        aSum = 0 
        for num in nums: 
            if num not in seen:
                if num <= k:
                    seen[num] = True
                    aSum += num
                    k += 1 
                else: break

        ans =  k*(k + 1)//2 - aSum
        
        return ans
