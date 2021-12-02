# https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        def helper(k):
            arr = workers[-k:]            
            tries = pills

            for elem in tasks[:k][::-1]:
                idx1 = bisect_left(arr, elem)
                if idx1 < len(arr):
                    arr.pop(idx1)
                elif tries > 0:
                    idx2 = bisect_left(arr, elem - strength)
                    if idx2 < len(arr):
                        arr.pop(idx2)
                        tries -= 1
                else:
                    return False

            return len(arr) == 0

        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()       
        
        start, end = 0, min(n, m) + 1
        while end - start > 1:
            m = (end + start)//2
            if helper(m):
                start = m
            else:
                end = m

        return start
