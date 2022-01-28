# https://leetcode.com/problems/largest-values-from-labels/

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        n = len(values)
        arr = [(values[i], labels[i]) for i in range(n)]
        
        arr.sort(reverse = True)
        
        counter = defaultdict(lambda: 0)
        size = 0 
        ans = 0 
        
        for (value, label) in arr: 
            counter[label] += 1 
            if counter[label] <= useLimit:
                size += 1
                ans += value
                if size >= numWanted:
                    break
                    
        return ans
