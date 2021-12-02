# https://leetcode.com/problems/number-of-lines-to-write-string/

class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        line = 1
        aux = 0
        n = len(S)
        
        for i in range(n):
            aux += widths[ord(S[i]) - ord("a")]
            if aux > 100:
                aux = widths[ord(S[i]) - ord("a")]
                line += 1
        
        return (line, aux)
