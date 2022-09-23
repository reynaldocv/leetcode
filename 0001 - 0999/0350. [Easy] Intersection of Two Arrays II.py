# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = defaultdict(lambda: 0)
        
        for num in nums1: 
            counter[num] += 1 
            
        ans = []
        
        for num in nums2: 
            if num in counter:
                counter[num] -= 1 
                ans.append(num)
                
                if counter[num] == 0: 
                    counter.pop(num)
                    
        return ans 
        
        
