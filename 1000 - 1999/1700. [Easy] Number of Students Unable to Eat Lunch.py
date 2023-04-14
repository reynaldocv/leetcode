# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        
        counter = defaultdict(lambda: 0)
        
        for student in students: 
            counter[student] += 1 
        
        ans = n
        
        for sandwich in sandwiches: 
            if counter[sandwich] > 0: 
                counter[sandwich] -= 1 
                
                ans -= 1 
                
            else: 
                return ans 
            
        return 0 
