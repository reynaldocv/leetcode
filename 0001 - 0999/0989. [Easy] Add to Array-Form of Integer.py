# https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        arr = [str(num[i]) for i in range(len(num))]
        num1 = int("".join(arr))
        arr = num1 + k
        ans = []
        if arr == 0: return [0]
        while arr > 0:
            r = arr % 10
            arr = arr // 10
            ans.insert(0, r)
        return ans
