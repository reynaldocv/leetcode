# https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        @cache
        def  helper(start, end):
            if start > end: 
                return 0 
            
            elif start == end: 
                return 1
        
            else: 
                counter = defaultdict(lambda: 0)
                arr = []
                
                ans = end - start
                
                for i in range(start, end + 1):
                    char = s[i]
                    
                    counter[char] += 1 
                    
                    old = counter[char] - 1 
                    
                    if old > 0: 
                        idx = bisect_left(arr, old)
                        
                        arr.pop(idx)
                        
                    insort(arr, counter[char])
                    
                    if arr[0] == arr[-1]:
                        ans = min(ans, 1 + helper(i + 1, end))
                        
                return ans 
            
        n = len(s)
        
        return helper(0, n - 1)
                        
                
