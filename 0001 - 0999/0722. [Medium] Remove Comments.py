# https://leetcode.com/problems/remove-comments/ 

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        comment = False 
        
        for (i, line) in enumerate(source):
            if not comment: 
                tmp = ""
            j = 0 
        
            while j < len(line):
                if comment: 
                    if line[j: j + 2] == "*/":
                        comment = False
                        j += 1 
                else: 
                    if line[j: j + 2] == "//":
                        break
                    elif line[j: j + 2] == "/*":
                        comment = True
                        j += 1 
                    else: 
                        tmp += line[j]
                
                j += 1 
                
            if tmp and not comment: 
                ans.append(tmp)
                
        return ans
