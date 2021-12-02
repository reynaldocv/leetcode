# https://leetcode.com/problems/queue-reconstruction-by-height/

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(reverse = True, key = lambda item: (item[0], -item[1])) 
        ans = [people[0]]
        
        for (h, cnt) in people[1:]:
            if cnt == 0: 
                ans.insert(0, (h, cnt))
            
            else: 
                j = 0
                counter = 0
                while ans and j < len(ans):
                    if ans[j][0] >= h: 
                        counter += 1                
                    j += 1
                    if counter == cnt: 
                        break

                ans.insert(j, (h, cnt))
            
        return ans
                
        
