# https://leetcode.com/problems/reward-top-k-students/

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive = {word for word in positive_feedback}
        negative = {word for word in negative_feedback}
        
        counter = defaultdict(lambda: 0)
        
        for (ith, sentence) in enumerate(report):
            student = student_id[ith]
            
            counter[student] += 0
            
            word = ""
                        
            for char in sentence + " ":
                if char == " ":
                    if word in negative: 
                        counter[student] -= 1 
                        
                    if word in positive: 
                        counter[student] += 3
                        
                    word = ""
                        
                else: 
                    word += char
                                    
        ans = [key for key in counter]
        
        ans.sort(key = lambda item: (-counter[item], item))
        
        return ans[: k]
            
            
            
