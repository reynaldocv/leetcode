# https://leetcode.com/problems/reorder-data-in-log-files/

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = {str(i):True for i in range(10)}
        arrl = []
        arrd = []
        for log in logs:
            idx = log.index(" ")
            aux = log[idx + 1:]
            if aux[0] in digit:
                arrd.append(log)
            else:
                arrl.append((aux, log[:idx + 1]))
        ans = []
        arrl.sort()
        for (a, b) in arrl:
            ans.append(b + a)
        ans.extend(arrd)
        return ans
        
