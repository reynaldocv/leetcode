# https://leetcode.com/problems/thousand-separator/

class Solution:
    def thousandSeparator(self, n: int) -> str:
        strn = str(n)
        l = len(strn)
        r = l % 3
        q = l//3
        ans = []
        if r > 0:
            ans.append(strn[:r])
        for i in range(q):
            ans.append(strn[i*3 + r: i*3 + r + 3])
        return ".".join(ans)
