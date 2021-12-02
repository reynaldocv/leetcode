# https://leetcode.com/problems/minimum-absolute-difference/

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        min_ = abs(arr[1] - arr[0])
        ans = [[arr[0], arr[1]]]
        l = len(arr)
        
        for i in range(2, l):
            dist = abs(arr[i] - arr[i - 1])
            if dist < min_:
                ans = [[arr[i - 1], arr[i]]]
                min_ = dist
            elif dist == min_:
                ans.append([arr[i - 1], arr[i]])
        
        return ans
        
