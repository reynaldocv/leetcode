# https://leetcode.com/problems/generate-parentheses/

class Solution:
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
                
                
