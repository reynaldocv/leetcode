# https://leetcode.com/problems/minimum-number-of-people-to-teach/

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        m = len(languages)
        friends = defaultdict(lambda:[])
        chatFriends = defaultdict(lambda: defaultdict(lambda: True))
                                
        for (a, b) in friendships: 
            friends[a - 1].append(b - 1)
            friends[b - 1].append(a - 1)
                                
        for user in range(m):
            for friend in friends[user]:
                go = False
                for lang in languages[user]:
                    if lang in languages[friend]:
                        go = True
                        break
                if go: 
                    chatFriends[user][friend] = True

        ans = inf
        
        for lang in range(1, n + 1):
            val = 0 
            for user in range(m):
                if len(friends[user]) != len(chatFriends[user]):
                    if lang not in languages[user]:
                        val += 1 
            ans = min(ans, val)
            
        return ans
