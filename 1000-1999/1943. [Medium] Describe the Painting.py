# https://leetcode.com/problems/describe-the-painting/

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        counter = {}
        for (start, end, color) in segments:
            counter[start] = counter.get(start, 0) + color
            counter[end] = counter.get(end, 0) - color
            
        idx = [*counter]
        idx.sort()
        start = idx[0]
        color = counter[idx[0]]
        ans = []
        for i in range(1, len(idx)):
            if color != 0:
                ans.append((start, idx[i], color))
            color += counter[idx[i]]
            start = idx[i]
        return ans
