# https://leetcode.com/problems/two-out-of-three/ 

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        counter = defaultdict(lambda: [0, 0, 0])
        
        for (i, nums) in enumerate([nums1, nums2, nums3]):
            for num in nums: 
                counter[num][i] = 1 
            
        ans = []
        
        for num in counter: 
            if sum(counter[num]) > 1: 
                ans.append(num)
                
        return ans
        
        
