# https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n, m, l = len(s), len(a), len(b)
        
        index = []
        
        for j in range(n - l + 1):
            if s[j: j + l] == b: 
                index.append(j)
        
        ans = []
        
        for i in range(n - m + 1):
            if s[i: i + m] == a: 
                
                idx = bisect_right(index, i)
                
                if idx < len(index):
                    if abs(index[idx] - i) <= k: 
                        ans.append(i)
                        
                if idx - 1 >= 0: 
                    if abs(index[idx - 1] - i) <= k: 
                        if not ans or (ans and ans[-1] != i):
                            ans.append(i)
                        
        return ans 
