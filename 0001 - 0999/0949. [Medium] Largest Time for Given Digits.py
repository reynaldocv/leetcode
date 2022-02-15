# https://leetcode.com/problems/largest-time-for-given-digits/

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        ans = ""
        
        for perm in permutations(arr):
            hours = perm[0]*10 + perm[1]
            minutes = perm[2]*10 + perm[3]
            
            if hours < 24 and minutes < 60: 
                strHours = "0" + str(hours) if hours < 10 else str(hours)
                strMinutes = "0" + str(minutes) if minutes < 10 else str(minutes)
                
                ans = max(ans, strHours + ":" + strMinutes)
                
        return ans
        
