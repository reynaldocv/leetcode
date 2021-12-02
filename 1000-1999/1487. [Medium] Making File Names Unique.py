# https://leetcode.com/problems/making-file-names-unique/

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        seen = {}
        
        for name in names: 
            if name in seen: 
                while name + "(" +  str(seen[name]) + ")" in seen: 
                    seen[name] += 1
                
                ans.append(name + "(" +  str(seen[name]) + ")")
                seen[name + "(" +  str(seen[name]) + ")"] = 1
            else: 
                ans.append(name)
                seen[name] = 1
                        
        return ans
