# https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        @cache 
        def helper(n):
            if n == 1: 
                return ["0", "1"]
            
            else: 
                ans = []
                
                for elem in helper(n - 1):
                    if elem[-1] == "0":
                        ans.append(elem + "1")
                        
                    else: 
                        ans.append(elem + "1")
                        ans.append(elem + "0")
                
                return ans 
            
        return helper(n)
