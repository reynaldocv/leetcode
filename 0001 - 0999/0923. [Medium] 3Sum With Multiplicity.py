# https://leetcode.com/problems/3sum-with-multiplicity/

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0 
        MOD = 10**9 + 7
        n = len(arr)
        arr.sort()
        for (i, numA) in enumerate(arr):
            T = target - numA
            j = i + 1
            k = n - 1
            while k - j > 0: 
                if arr[j] + arr[k] < T: 
                    j += 1
                elif arr[j] + arr[k] > T:
                    k -= 1
                elif arr[j] != arr[k]:
                    countLeft = countRight = 1
                    while j + 1 < k and arr[j] == arr[j + 1]:
                        countLeft, j = countLeft + 1, j + 1
                    while j < k - 1 and arr[k - 1] == arr[k]:
                        countRight, k = countRight + 1, k - 1   
                    ans += countLeft*countRight
                    ans %= MOD
                    j += 1
                    k -= 1
                else: 
                    ans += (k - j + 1)*(k - j)//2
                    ans %= MOD
                    break
        
        return ans % MOD
                    
      
