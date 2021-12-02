# https://leetcode.com/problems/split-array-into-fibonacci-sequence/

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def helper(prev, cur, s, arr):            
            nonlocal ans
            if 0 <= int(cur) < 2**31:
                if cur == s: 
                    ans = list(arr + [cur])
                    return True

                elif cur in s: 
                    if s.index(cur) == 0: 
                        prev, cur = cur, str(int(cur) + int(prev))
                        if helper(prev, cur, s[len(prev):], arr + [prev]):
                            return 
                
        ans = []
        
        n = len(num)
        for i in range(1, n - 2):
            for j in range(i + 1, n - 1):                
                prev = num[:i]
                cur = num[i:j]
                condition1 = prev[0] != "0" or (prev[0] == "0" and len(prev) == 1)
                condition2 = cur[0] != "0" or (cur[0] == "0" and len(cur) == 1)
                
                if condition1 and condition2: 
                    newCur = str(int(prev) + int(cur))                
                    helper(cur, newCur, num[j:], [num[:i], num[i:j]])
        
        return ans
