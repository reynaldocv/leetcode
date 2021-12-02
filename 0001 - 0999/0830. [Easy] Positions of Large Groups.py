# https://leetcode.com/problems/positions-of-large-groups/

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        S = s + " "
        n = len(S)
        aux = ""
        word = ""
        start = -1
        ans = []
        for i in range(n):
            if aux == S[i]:
                word += aux
            else: 
                if len(word) >= 3: 
                    ans.append((start, i - 1))                    
                aux = S[i]
                start = i
                word = S[i]
        return ans
