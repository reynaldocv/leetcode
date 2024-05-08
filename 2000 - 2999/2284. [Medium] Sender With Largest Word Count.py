# https://leetcode.com/problems/sender-with-largest-word-count/

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        counter = defaultdict(lambda: 0)
        
        ans = (0, "$")
        
        for (ith, sender) in enumerate(senders):
            message = messages[ith]
            
            prev = ""
            cnt = 0 
            
            for char in message + " ":
                if char == " ":
                    if prev: 
                        cnt += 1 
                        
                        prev = ""
                        
                else: 
                    prev += char 
                    
            counter[sender] += cnt
            
            ans = max(ans, (counter[sender], sender))
            
        return ans[1]
                    
            
    
