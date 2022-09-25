# https://leetcode.com/problems/binary-watch/

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        seen = {0: 8, 1: 4, 2: 2, 3:1, 4:32, 5: 16, 6: 8, 7: 4, 8: 2, 9: 1}
        
        ans = []
        
        for comb in combinations([i for i in range(10)], turnedOn):            
            hours = 0 
            minutes = 0 
            
            for value in comb: 
                if value <= 3: 
                    hours += seen[value]
                else: 
                    minutes += seen[value]
                
            tmp = ""
            
            if hours < 12 and minutes < 60: 
                tmp = str(hours)
            
                if minutes <= 9:
                    tmp += ":0" + str(minutes)
                else: 
                    tmp += ":" + str(minutes)

                ans.append(tmp)

        return ans
            
