# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def helper(value):
            cnt = 0 
            
            for num in nums1: 
                if num == 0: 
                    if value >= 0: 
                        cnt += n
                    
                else: 
                    tmp = abs(num)

                    if num < 0: 
                        cnt += bisect_right(negative, value//tmp)

                    else: 
                        cnt += bisect_right(nums2, value//tmp)

            return cnt 
        
        n = len(nums2)
        
        idx = bisect_left(nums2, 0)
        
        negative = [-num for num in nums2][:: -1]
        
        start = -(10**5**2)
        end = (10**5)**2
        
        while end - start > 1: 
            mid = (end + start)//2
            
            if helper(mid) < k: 
                start = mid 
                
            else: 
                end = mid 
        
        return end 
                                        
                    
                                        
                                        
        
                
                
                
        
        
        
        
        
        
       
