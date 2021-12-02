# https://leetcode.com/problems/count-good-triplets/

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:        
        ans = 0
        l = len(arr)
        for i in range(l - 2):
            for j in range(i + 1, l - 1):
                for k in range(j + 1, l):
                    if (-a <= arr[i] - arr[j] <= a) and (-b <= arr[j] - arr[k] <= b) and (-c <= arr[i] - arr[k] <= c):
                        ans += 1
        return ans
