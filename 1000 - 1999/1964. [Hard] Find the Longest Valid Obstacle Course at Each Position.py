# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        arr = []
        ans = []
        for obstacle in obstacles: 
            idx = bisect_right(arr, obstacle)
            ans.append(idx + 1)  
            if idx != len(arr):
                arr[idx] = obstacle
            else: 
                arr.append(obstacle)
            
        return ans
        
