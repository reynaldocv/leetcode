# https://leetcode.com/problems/array-of-doubled-pairs/

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counter = {}
        for num in arr: 
            counter[num] = counter.get(num, 0) + 1
        arr.sort(key = abs)
        print(arr)
        n = len(arr)
        for i in range(n):
            if counter[arr[i]] > 0:                                    
                counter[arr[i]] -= 1
                if 2*arr[i] in counter and counter[2*arr[i]] > 0:
                    counter[2*arr[i]] -= 1
                else:
                    return False 
        return True 
