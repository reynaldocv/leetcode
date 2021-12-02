# https://leetcode.com/problems/swap-nodes-in-pairs/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head == None or head.next == None: 
            return head
        else: 
            ans = prev = ListNode(0, head)
            cur = head
            post = head.next
            i = 0
            while post: 
                if i == 0:
                    prev.next, post.next, cur.next = post, cur, post.next
                    prev = prev.next
                    post = cur.next                      
                else:
                    prev = prev.next
                    cur = cur.next
                    post = post.next
                i  = (i + 1) % 2

            return ans.next

        
