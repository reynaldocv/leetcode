# https://leetcode.com/problems/find-the-number-of-good-pairs-ii/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        counter = defaultdict(lambda: 0)
        
        for num in nums2: 
            counter[num*k] += 1 
            
        ans = 0 
        
        for num in nums1: 
            for i in range(1, isqrt(num) + 1):
                if num % i == 0: 
                    ans += counter[i]
                    
                    if i**2 != num: 
                        ans += counter[num//i]
                        
        return ans 
        
