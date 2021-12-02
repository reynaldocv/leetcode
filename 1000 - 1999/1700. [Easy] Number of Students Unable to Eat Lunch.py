# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        if students.count(1) == sandwiches.count(1):
            return 0
        
        counter = {}
        for student in students:
            counter[student] = counter.get(student, 0) + 1
        
        for i in range(n):
            if sandwiches[i] in counter and counter[sandwiches[i]] > 0:
                counter[sandwiches[i]] -= 1                
            else:
                return n - i

        return 0
