# https://leetcode.com/problems/circular-array-loop/

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
             
        def findloop(i): # find the loop 
            slow = fast = i
            sign = nums[i]
            while True:
                for _ in range(2):
                    fast = (fast + nums[fast]) % n
                    if sign * nums[fast] <= 0:
                        return False
                slow = (slow + nums[slow]) % n

                if slow == fast:
                    return True

        def changeToZero(i):
            sign = nums[i]
            while sign * nums[i] > 0:
                nums[i] = 0
                i = (i + nums[i]) % n
                
        n = len(nums)
        
        for i in range(n): 
            if (i + nums[i]) % n == i:
                nums[i] = 0
        
        for i in range(n):
            if nums[i] != 0:
                if findloop(i):
                    return True
                else:
                    changeToZero(i)

        return False

