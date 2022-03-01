# https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(arr1, arr2):
            counter = defaultdict(lambda: 0)
            squares = defaultdict(lambda: 0)

            for num in arr1: 
                counter[num] += 1 
                
            for num in arr2:
                squares[num**2] += 1 
                
            ans = 0 
            for square in squares: 
                limit = int(square**.5)
                cnt = 0 
                for i in range(1, limit):
                    if square % i == 0: 
                        cnt += counter[i]*counter[square//i]

                cnt += counter[limit]*(counter[limit] - 1)//2
                ans += cnt*squares[square]
            
            return ans 
        
        return helper(nums1, nums2) + helper(nums2, nums1)
