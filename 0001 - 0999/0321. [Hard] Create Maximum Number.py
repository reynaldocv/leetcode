# https://leetcode.com/problems/create-maximum-number/

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def helper(arr, k):
            ans = []
            for (i, num) in enumerate(arr):
                while ans and ans[-1] < num and len(ans) + len(arr) - i > k:
                    ans.pop()
                
                if len(ans) < k: 
                    ans.append(num)
                    
            return ans
        
        ans = [0]*k
        
        for i in range(k + 1):
            if k - len(nums2) <= i <= len(nums1):
                arr1 = helper(nums1, i)
                arr2 = helper(nums2, k - i)
                idx1 = idx2 = 0 
                aux = []
                while idx1 < len(arr1) or idx2 < len(arr2):
                    if arr1[idx1:] > arr2[idx2:]:
                        aux.append(arr1[idx1])
                        idx1 += 1
                    else: 
                        aux.append(arr2[idx2])
                        idx2 += 1
                ans = max(ans, aux)
                
        return ans
                    
