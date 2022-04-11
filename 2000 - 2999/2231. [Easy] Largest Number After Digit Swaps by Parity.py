# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

class Solution:
    def largestInteger(self, num: int) -> int:
        positions = [int(char) % 2 for char in str(num)]
        odds = []
        evens = []
        
        for char in str(num):
            if int(char) % 2 == 1: 
                odds.append(int(char))
            else: 
                evens.append(int(char))
                
        odds.sort(reverse = True)
        evens.sort(reverse = True)
        
        ans = ""
        i, j = 0, 0
        
        for isOdd in positions:
            if isOdd: 
                ans += str(odds[i])
                i += 1 
            else: 
                ans += str(evens[j])
                j += 1
                
        return int(ans)
