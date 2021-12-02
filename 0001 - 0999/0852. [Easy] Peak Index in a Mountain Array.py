# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = len(arr)
        pos = 1
        ans = 0
        aux = 0
        while pos < l - 1:
            if arr[pos - 1] < arr[pos] and arr[pos] > arr[pos + 1] and arr[pos] > aux:
                aux = arr[pos]
                ans = pos
                break
            pos += 1
        return ans
        
