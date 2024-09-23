# https://leetcode.com/problems/report-spam-message/

class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        seen = {word for word in bannedWords}
        
        cnt = 0
        
        for word in message:
            if word in seen:
                cnt += 1
                
        return cnt >= 2
                
