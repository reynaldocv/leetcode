# https://leetcode.com/problems/find-the-integer-added-to-array-ii/

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        minNum = min(nums2)
        
        counter = defaultdict(lambda: 0)        
        
        minElems = []
        
        for num in nums1: 
            counter[num] += 1 
            
            insort(minElems, num)
            
            minElems = minElems[: 3]
            
        ans = inf
            
        for (i, num) in enumerate(minElems): 
            count = counter.copy()
            
            ratio = minNum - num
            
            go = True 
            
            for num in nums2: 
                count[num - ratio] -= 1 
                
                if count[num - ratio] < 0:   
                    go = False
                    
                    break 
                    
            if go: 
                ans = min(ans, ratio)
                
        return ans
            
            
        
        
