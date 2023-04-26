# https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def helper(value, i):
            nonlocal ans
            
            if i == n: 
                ans += value 
                
            else: 
                for j in range(i, n):
                    helper(value^nums[j], j + 1)
        
        nums.append(0)
        
        n = len(nums)
        
        ans = 0 
        
        helper(0, 0)
        
        return ans
   
class Solution2:
    def subsetXORSum(self, nums: List[int]) -> int:       
        n = len(nums)
        
        arr = []
        
        for i in range(n):
            arr.extend(list(combinations(nums, i + 1)))
        
        ans = 0
        for elem in arr: 
            elem = list(elem)
            
            aux = elem[0]
            for i in range(1, len(elem)): 
                aux = elem[i]^aux
            
            ans += aux               
                
        return ans
