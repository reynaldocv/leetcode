# https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: 
            return None
        
        newNodes = {}
        temp, cur = head, head
        while temp: 
            newNodes[temp] = Node(temp.val)
            temp = temp.next
        
        ans = cur
        while cur: 
            newNodes[cur].next = newNodes[cur.next] if cur.next else None
            newNodes[cur].random = newNodes[cur.random] if cur.random else None
            cur = cur.next
        
        return newNodes[ans]
            
