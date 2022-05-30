# https://leetcode.com/problems/sender-with-largest-word-count/

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        counter = defaultdict(lambda: 0)
        
        n = len(messages)
        
        ans = (0, "$")
        for i in range(n):
            arr = messages[i].split(" ")
            counter[senders[i]] += len(arr)
            
            ans = max(ans, (counter[senders[i]], senders[i]))
            
        return ans[1]
    
    
