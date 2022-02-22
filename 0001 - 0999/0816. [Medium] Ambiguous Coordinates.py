# https://leetcode.com/problems/ambiguous-coordinates/

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def helper(string):
            if string == "0":
                return ["0"]
            elif string[0] == string[-1] == "0":
                return []
            elif string[0] == "0": 
                return [string[0] + "." +string[1:]]
            elif string[-1] == "0":
                return [string]
            else: 
                ans = [string]
                for i in range(1, len(string)):
                    ans.append(string[:i] + "." + string[i:])
                
                return ans
        
        ans = []
        s = s[1:-1]
        
        n = len(s)
        for i in range(1, n):
            left = helper(s[:i])
            right = helper(s[i:])
            for l in left: 
                for r in right: 
                    ans.append("(" + l + ", " + r + ")")
        
        return ans
