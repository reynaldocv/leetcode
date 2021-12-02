# https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution(object):
    def minSetSize(self, arr):
        counter = {}
        for num in arr:
            counter[num] = counter.get(num, 0) + 1
        frequency = [*counter.values()]    
        frequency.sort(reverse = True)
        
        ans = 0
        sumFrequencies = 0
        for i in range(len(frequency)):
            freq = frequency[i]
            if sumFrequencies >= len(arr)//2:
                break
            else:
                ans +=1
                sumFrequencies += freq
        
        return ans
