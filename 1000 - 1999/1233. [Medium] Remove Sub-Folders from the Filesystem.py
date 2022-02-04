# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ans = []
        folder.sort()
        
        for x in folder: 
            if not ans or not x.startswith(ans[-1]+"/"): 
                ans.append(x)
                
        return ans 
