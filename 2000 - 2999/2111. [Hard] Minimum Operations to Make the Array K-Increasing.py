# https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/

class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        def helper(nums):            
            sub = []
            for (i, num) in enumerate(nums):
                if len(sub) == 0 or sub[-1] <= num:
                    sub.append(num)
                else: 
                    idx = bisect_right(sub, num)
                    sub[idx] = num
            
            return len(sub)
        
        ans = 0 
        for i in range(k):
            aux = arr[i::k]
            ans += len(aux) - helper(aux)
            
        return ans
