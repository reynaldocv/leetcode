# https://leetcode.com/problems/find-palindrome-with-fixed-length/

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        def helper(th, n):
            m = n//2
            ans = 0
            if n % 2 == 0: 
                val = 10**(m - 1) + th - 1
                strVal = str(val)
                
                ans = int(strVal + strVal[::-1])
            else: 
                val = 10**m + th - 1
                strVal = str(val)
                
                ans = int(strVal + strVal[:-1][::-1])
                
            if len(str(ans)) == n: 
                return ans 
            else: 
                return -1
            
        ans = []
        for query in queries: 
            ans.append(helper(query, intLength))
            
        return ans 
                
