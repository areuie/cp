# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        priQueue = []

        for i, l in enumerate(lists):
            if l:
                heapq.heappush(priQueue, (l.val, i, l))
        
        pseudoNode = ListNode(0, None)
        prev = pseudoNode

        while priQueue:
            val, i, node = heapq.heappop(priQueue)
            prev.next = node
            prev = prev.next

            if node.next:
                heapq.heappush(priQueue, (node.next.val, i, node.next))

        return pseudoNode.next


