# https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        prev = inf
        turn = False
        n = len(nums)
        
        m = 0 
        for num in nums:
            if turn == False: 
                prev = num
                m += 1   
                turn = True
            else: 
                if prev != num:
                    m += 1 
                    turn = False 
                    prev = inf
        
        if m % 2 == 1: 
            m -= 1 
            
        return n - m 
