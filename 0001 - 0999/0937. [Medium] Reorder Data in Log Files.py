# https://leetcode.com/problems/reorder-data-in-log-files/

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def helper(log):
            words = log.split(" ")
            
            return (" ".join(words[1: ]), words[0])
            
        letters = []
        digits = []
        
        for (ith, log) in enumerate(logs):
            words = log.split(" ")
            
            if words[1].isdigit():
                digits.append(log)
                
            else:
                letters.append(log)
      
        letters.sort(key = lambda item: helper(item))
        
        return letters + digits
        
        
        
                              
                               
                             
