# https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        arr.sort(key = lambda item: abs(item - x))
        ans = []
        
        print(arr)
        
        for num in arr:
            if num < x: 
                ans.insert(0, num)
            else: 
                ans.append(num)
                
            if len(ans) == k: 
                break

        return ans

        
        
