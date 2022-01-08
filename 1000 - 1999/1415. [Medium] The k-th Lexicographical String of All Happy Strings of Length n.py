# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def helper(m):
            if m == 1: 
                return ["a", "b", "c"]
            else: 
                ans = []
                for aux in helper(m - 1):
                    for char in "abc":
                        if aux[-1] != char: 
                            ans.append(aux + char)
                return ans
            
        arr = helper(n)
        
        return arr[k - 1] if k - 1 < len(arr) else ""
        
        
        
