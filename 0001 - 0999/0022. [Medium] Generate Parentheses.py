# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        @cache 
        def helper(x):
            if x == 1: 
                return ["()"]
            
            else: 
                ans = set()
                
                for i in range(1, x):
                    
                    for left in helper(i):
                        for right in helper(x - i):
                            ans.add(left + right)

                for center in helper(x - 1):
                    ans.add("(" + center + ")")
                
                return ans 
            
        return helper(n)
            
class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        dic = {1: (["()"])}
               
        for i in range(2, n + 1):
            dic[i] = set([])    
            
            for j in range(1, i):
                for pre in dic[j]:
                    for post in dic[i - j]:
                        dic[i].add(pre + post)
                        
            for word in dic[i - 1]:
                dic[i].add("(" + word + ")")
            
        return dic[n]
                
                
