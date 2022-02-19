# https://leetcode.com/problems/remove-comments/ 

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        comment = False 
        
        for line in source:
            if not comment: 
                tmp = ""
            i = 0 
        
            while i < len(line):
                if comment: 
                    if line[i: i + 2] == "*/":
                        comment = False
                        i += 1 
                else: 
                    if line[i: i + 2] == "//":
                        break
                    elif line[i: i + 2] == "/*":
                        comment = True
                        i += 1 
                    else: 
                        tmp += line[i]
                
                i += 1 
                
            if tmp and not comment: 
                ans.append(tmp)
                
        return ans
