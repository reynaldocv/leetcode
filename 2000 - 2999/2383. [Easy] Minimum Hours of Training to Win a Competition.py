# https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        ans = 0
        
        totalEnergy = sum(energy)
        
        if initialEnergy <= totalEnergy:
            ans += (totalEnergy - initialEnergy + 1)
            
        for exp in experience:
            if initialExperience <= exp:
                ans += (exp - initialExperience + 1)
                initialExperience = exp + 1
                
            initialExperience += exp
            
        return ans
