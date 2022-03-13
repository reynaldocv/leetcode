# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        index = [i for (i, num) in enumerate(nums) if num == key]
        arr = set()
        n = len(nums)
        
        for idx in index: 
            for i in range(k + 1):
                val = idx - i
                if val >= 0: 
                    arr.add(val)
                val = idx + i
                if val < n:
                    arr.add(val)
                    
        ans = list(arr)
        ans.sort()
        
        return ans
        
        
