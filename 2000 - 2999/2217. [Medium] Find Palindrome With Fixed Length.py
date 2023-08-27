# https://leetcode.com/problems/find-palindrome-with-fixed-length/

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        ans = []
        
        m = intLength//2

        if intLength % 2 == 1:            
            num = 10**m
        
        else: 
            num = 10**(m - 1)

        for querie in queries: 
            tmp = num + querie - 1
            
            if len(str(tmp)) != len(str(num)):
                ans.append(-1)
            
            elif intLength % 2 == 1:
                ans.append(int(str(tmp) + str(tmp)[::-1][1: ]))
                
            else: 
                ans.append(int(str(tmp) + str(tmp)[::-1]))
                
        return ans
