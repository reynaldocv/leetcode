# https://leetcode.com/problems/3sum-with-multiplicity/

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        ans = 0 
        n = len(arr)
        
        arr.sort()
        
        for (i, num) in enumerate(arr):
            aSum = target - num
            start = i + 1
            end = n - 1
            while end > start:
                if arr[start] + arr[end] < aSum: 
                    start += 1 
                elif arr[start] + arr[end] > aSum:
                    end -= 1 
                elif arr[start] != arr[end]:
                    left = 0
                    while start < end and arr[start] == arr[start + left]:
                        left += 1 
                    
                    right = 0 
                    while start < end and arr[end] == arr[end - right]:
                        right += 1 
                    
                    ans = (ans + left*right) % MOD
                    start += left
                    end -= right
                
                else: 
                    ans = (ans + (end - start + 1)*(end - start)//2)
                    break 
            
        return ans % MOD
