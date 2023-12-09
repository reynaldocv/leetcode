# https://leetcode.com/problems/find-common-elements-between-two-arrays/

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = defaultdict(lambda: 0)
        counter2 = defaultdict(lambda: 0)
        
        for num in nums1: 
            counter1[num] += 1 
            
        for num in nums2:
            counter2[num] += 1 
            
        ans = [0, 0]
        
        tmp = 0
        
        for num in nums1: 
            if counter2[num] >= 1: 
                tmp += 1 
                
        ans[0] = tmp
        
        tmp = 0
        
        for num in nums2: 
            if counter1[num] >= 1: 
                tmp += 1 
                
        ans[1] = tmp
        
        return ans 
        


