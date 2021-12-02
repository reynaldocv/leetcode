# https://leetcode.com/problems/decode-xored-array/

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        aux = first
        for i in range(len(encoded)):
            b = aux^encoded[i]
            ans.append(b)
            aux = b
        return ans
        
