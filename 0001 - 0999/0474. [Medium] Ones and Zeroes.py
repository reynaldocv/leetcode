# https://leetcode.com/problems/ones-and-zeroes/

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        ans = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for word in strs:             
            count1 = len([1 for w in word if w == "1"])
            count0 = len(word) - count1           
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i - count0 >= 0 and j - count1 >= 0: 
                        ans[i][j] = max(ans[i][j], 1 + ans[i - count0][j - count1])
            
        return ans[m][n]
