# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

class Solution:
    def digitCount(self, num: str) -> bool:
        counter = defaultdict(lambda: 0)
        for char in num: 
            counter[char] += 1 
            
        n = len(num)
        
        for i in range(n):
            if counter[str(i)] != int(num[i]):
                return False 
            
        return True 
