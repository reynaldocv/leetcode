# https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans, j, ntarget = [], 0, len(target)
        
        for i in range(1, n + 1):           
            if i == target[j]:
                j += 1
                ans.append("Push")
                if j == ntarget: 
                    break
            else: 
                ans.append("Push")
                ans.append("Pop")
        return ans
                
