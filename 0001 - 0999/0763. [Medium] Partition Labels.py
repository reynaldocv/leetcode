# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = defaultdict(lambda: -1)
        
        for (i, char) in enumerate(s):
            last[char] = i 
            
        start = -1 
        end = -1
        
        ans = []
        
        for (i, char) in enumerate(s):
            end = max(end, last[char])
            
            if i == end: 
                ans.append(i - start)
                
                start = i
                
        return ans 
        
