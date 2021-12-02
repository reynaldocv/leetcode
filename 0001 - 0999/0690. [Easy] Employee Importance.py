# https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dic = {}
        for employee in employees: 
            dic[employee.id] = employee
        
        people, visited, ans =  [id], {}, 0
        while len(people) > 0:
            id = people.pop()
            if id not in visited:
                visited[id] = True
                person = dic[id]
                ans += person.importance
                for sub in person.subordinates: 
                    people.append(sub)
        return ans
