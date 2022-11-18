# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        counter = [0, 0]
        cnt = [0, 0]

        for char in s: 
            if char == "0":
                cnt[0] += 1 
                cnt[1] = 0 

            else:
                cnt[0] = 0 
                cnt[1] += 1 

            counter[0] = max(counter[0], cnt[0])
            counter[1] = max(counter[1], cnt[1])
                
        return counter[0] < counter[1]
            
