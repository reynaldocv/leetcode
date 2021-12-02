# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ending = {}
        
        for (i, char) in enumerate(s):
            ending[char] = i
        
        start = 0 
        end = 0 
        ans = []
        
        for (i, char) in enumerate(s):
            end = max(end, ending[char])
            if end == i: 
                ans.append(end - start + 1)
                start = i + 1
        
        return ans
        
