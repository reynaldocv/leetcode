# https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/

class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        
        arr = [energyDrinkA, energyDrinkB]
        
        arr[0][1] += arr[0][0]
        arr[1][1] += arr[1][0]
        
        ans = max(arr[0][1], arr[1][1])
        
        for i in range(2, n):
            arr[0][i] += max(arr[0][i - 1], arr[1][i - 2])
            arr[1][i] += max(arr[1][i - 1], arr[0][i - 2])
            
            ans = max(ans, arr[0][i], arr[1][i])
          
        return ans 
