# https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = set([])
        counter = defaultdict(lambda: 0)
        for num in nums: 
            counter[num] += 1
            if counter[num] > n//3:
                ans.add(num)
                
        return ans
        
        
        
