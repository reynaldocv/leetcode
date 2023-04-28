# https://leetcode.com/problems/find-the-difference-of-two-arrays/

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        counter = defaultdict(lambda: [0, 0])
        
        for (i, nums) in enumerate([nums1, nums2]):
            for num in nums: 
                counter[num][i] = 1
                
        ans = [[], []]
        
        for key in counter: 
            if sum(counter[key]) == 1: 
                if counter[key][0] == 1: 
                    ans[0].append(key)
                    
                else: 
                    ans[1].append(key)
        
        return ans 
        
