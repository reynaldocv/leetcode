# https://leetcode.com/problems/falling-squares/

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        n = len(positions)
        
        arr = [0 for _ in range(n)]
        
        for (i, (left, size)) in enumerate(positions):
            right = left + size
            arr[i] += size
            
            for j in range(i + 1, n):
                (left2, size2) = positions[j]
                right2 = left2 + size2
                
                if left2 < right and left < right2: 
                    arr[j] = max(arr[j], arr[i])
        
        ans = []
        for num in arr: 
            if ans: 
                ans.append(max(ans[-1], num))
            else: 
                ans.append(num)
                
        return ans
