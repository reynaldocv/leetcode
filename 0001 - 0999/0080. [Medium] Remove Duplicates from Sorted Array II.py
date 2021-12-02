# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 0 
        pointer = 0 
        n = len(nums)
        aux = -inf
        ans = 0
        for i in range(n):
            if aux != nums[i]:
                aux = nums[i]
                counter = 1                
                nums[pointer] = aux
                ans += 1
                pointer += 1
            else: 
                counter += 1
                if counter <= 2: 
                    nums[pointer] = aux
                    ans += 1
                    pointer += 1
        return ans
                
            
            
