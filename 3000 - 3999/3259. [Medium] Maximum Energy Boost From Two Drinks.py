# https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/

class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        arr = [energyDrinkA, energyDrinkB]
        
        n = len(energyDrinkA)
        
        arr[0][1] += arr[0][0]
        arr[1][1] += arr[1][0]
        
        for i in range(2, n):
            arr[0][i] += max(arr[0][i - 1], arr[1][i - 2])
            arr[1][i] += max(arr[1][i - 1], arr[0][i - 2])
          
        return max(max(arr[0]), max(arr[1]))
