# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
            
        for i in range(n - 1, k - 1, -1):
            energy[i - k] += energy[i]
        
        return max(energy)
        
