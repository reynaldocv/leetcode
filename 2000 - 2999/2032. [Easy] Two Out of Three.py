# https://leetcode.com/problems/two-out-of-three/ 

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        counter = defaultdict(lambda: [0, 0, 0])
        
        for num in nums1: 
            counter[num][0] = 1
        
        for num in nums2:
            counter[num][1] = 1
        
        for num in nums3:
            counter[num][2] = 1
            
        ans = []
        for num in counter: 
            if sum(counter[num]) >= 2: 
                ans.append(num)
                
        return ans
        
        
