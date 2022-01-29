# https://leetcode.com/problems/can-make-palindrome-from-substring/

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        def helper(i, j):
            ans = {}
            for key in counter[i]:
                diff = counter[i][key] - counter[j][key]
                if diff > 0:
                    ans[key] = diff
                
            return ans
            
        cnt = defaultdict(lambda: 0)
        counter = [cnt]
        for char in s: 
            cnt = counter[-1].copy()
            cnt[char] += 1 
            counter.append(cnt)
                
        ans = []
        for (start, end, k) in queries: 
            end += 1 
            cnt = helper(end, start)
            
            total = 0 
            for key in cnt:
                total += cnt[key] % 2
                
            ans.append(total//2 <= k)
            
        return ans
                
            
            
            
            
        
