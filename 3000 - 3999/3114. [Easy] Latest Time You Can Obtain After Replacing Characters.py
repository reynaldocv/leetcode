# https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/

class Solution:
    def findLatestTime(self, s: str) -> str:
        def helper(word, tmp):
            for i in range(2):
                if tmp[i] != "?": 
                    if tmp[i] != word[i]:
                        return False 
                    
            return True
        
        options = ["0" + str(i) for i in range(10)] + ["10", "11"]
        
        first = ""
        second = ""
        
        for word in options: 
            if helper(word, s[: 2]):
                first = word                
                        
        second += "5" if s[3] == "?" else s[3]
        second += "9" if s[4] == "?" else s[4]
            
        return first + ":" + second
        
            
        
        

        
        
