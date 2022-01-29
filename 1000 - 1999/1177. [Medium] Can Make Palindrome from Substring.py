# https://leetcode.com/problems/can-make-palindrome-from-substring/

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        def helper(i, j):
            ans = [0]*26
            for k in range(26):
                ans[k] = counter[i][k] - counter[j][k]
                
            return tuple(ans)
            
        cnt = (0, )*26
        counter = [cnt]
        for char in s: 
            i = ord(char) - ord("a")
            cnt = cnt[:i] + (cnt[i] + 1, ) + cnt[i + 1:]
            counter.append(cnt)
        
        ans = []
        for (start, end, k) in queries: 
            end += 1 
            cnt = helper(end, start)
            total = 0 
            for i in range(26):
                total += cnt[i] % 2
                
            ans.append(total//2 <= k)
            
        return ans
