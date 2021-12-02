# https://leetcode.com/problems/1-bit-and-2-bit-characters/submissions/

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        if bits[n - 1] != 0: return False
        
        bits = [str(bits[i]) for i in range(n - 1)]
        exist = {"": True}
        for i in range(n - 1):            
            aux = "".join(bits[:i])
            if aux in exist: 
                if bits[i] == "0":
                    exist[aux + "0"] = True
                if i + 1 < n - 1:
                    pair = bits[i] + bits[i + 1]
                    if pair == "10" or pair == "11":
                        exist[aux + pair] = True
        
        return True if "".join(bits) in exist else False
                
        
        
