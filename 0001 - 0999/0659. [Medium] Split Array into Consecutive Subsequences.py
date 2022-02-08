# https://leetcode.com/problems/split-array-into-consecutive-subsequences/

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = defaultdict(lambda: 0)
        hypo = defaultdict(lambda: 0)
    
        for num in nums:
            freq[num] += 1

        for num in nums:
            if freq[num] == 0:
                continue

            if hypo[num] > 0:
                hypo[num] -= 1
                hypo[num + 1] += 1
                freq[num] -= 1
                
            elif freq[num] > 0 and freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num] -= 1
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                hypo[num + 3] += 1
            else:
                return False
       
        return True
