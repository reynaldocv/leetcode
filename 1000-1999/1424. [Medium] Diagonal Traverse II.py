# https://leetcode.com/problems/diagonal-traverse-ii/

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        arr = []
        
        for i in range(n):
            for (j, num) in enumerate(nums[i]):
                ii = (i + j)*(i + j + 1)//2 + 1
                arr.append((ii + j, num))
                
        arr.sort()
        ans = [num for (_, num) in arr]
        
        return ans
        
                
            
            
        
        
            
