# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/ 

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arr = [tuple(points[0])]
        
        for (x1, y1) in points[1:]:
            if arr: 
                idx = bisect_left(arr, (x1, 0))
                if idx < len(arr):
                    (x0, y0) = arr[idx]
                else: 
                    (x0, y0) = arr.pop()
                    if max(x0, x1) <= min(y0, y1):
                        insort(arr, (max(x0, x1), min(y0, y1)))
                    else:
                        insort(arr, (x0, y0))
                        insort(arr, (x1, y1))
            else: 
                arr.append((x1, y1))
        
        return len(arr)
                
        
            
