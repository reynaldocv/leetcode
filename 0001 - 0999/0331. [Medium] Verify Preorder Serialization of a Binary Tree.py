# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        arr = preorder.split(",")
        n = len(arr)
        for i in range(n):
            if arr[i] != "#":
                arr[i] = "d"
        aux = ",".join(arr)
        
        while "d,#,#" in aux: 
            aux = aux.replace("d,#,#", "#")
        
        return True if aux == "#" else False
        
