# https://leetcode.com/problems/intervals-between-identical-elements/

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        
        index = defaultdict(lambda: [])
        for (i, num) in enumerate(arr): 
            index[num].append(i)
            
        ans = [0 for _ in range(n)]
        
        for num in index: 
            arr = index[num]
            left = 0 
            right = sum(arr)
            m = len(arr)
            for (i, idx) in enumerate(arr):
                right -= arr[i]
                ans[idx] = i*idx - left + right - (m - i - 1)*idx
                left += arr[i]
            
        return ans
