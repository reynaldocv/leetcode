# https://leetcode.com/problems/contains-duplicate-iii/

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        arr = [(nums[i], i) for i in range(n)]
        arr.sort(reverse = True)
        
        for i in range(n - 1):
            j = i + 1
            while j < n and arr[i][0] - arr[j][0] <= t: 
                if abs(arr[i][1] - arr[j][1]) <= k:
                    return True
                j += 1
        
        return False
                
        
        
