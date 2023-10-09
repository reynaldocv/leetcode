# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(arr, aSum, i):
            if aSum ==  0: 
                ans.append(arr.copy())
                
            elif aSum > 0: 
                for j in range(i, n):
                    if counter[nums[j]] > 0: 
                        counter[nums[j]] -= 1                         
                        arr.append(nums[j])
                        
                        helper(arr, aSum - nums[j], j)
                        
                        arr.pop() 
                        counter[nums[j]] += 1 
                        
        counter = defaultdict(lambda: 0)
        
        for num in candidates: 
            counter[num] += 1 
            
        nums = [key for key in counter]
        n = len(nums)
        
        ans = []
        
        helper([], target, 0)
        
        return ans 
            
