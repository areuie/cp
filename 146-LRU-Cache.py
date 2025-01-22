class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.lookup = {} # dict to find val to node pair
        #connect head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        
        node = self.lookup[key]
        
        #move to front of list
        self.remove(node)
        self.put(node.key, node.val)
        
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            node = self.lookup[key]
            self.remove(node)
            node.val = value
            #update dict
            #put to front
        elif len(self.lookup) >= self.capacity:
            self.remove(self.tail.prev)

        node = ListNode(key, value)
        #you need to add the node to the head and the node to the 2nd value
        secondNode = self.head.next
        secondNode.prev = node

        #node to second and head
        node.next = secondNode
        node.prev = self.head

        #head to node
        self.head.next = node

        self.lookup[key] = node

    def remove(self, node):
        #connecting the adj nodes together
        leftNode = node.prev
        rightNode = node.next

        leftNode.next, rightNode.prev = rightNode, leftNode

        del self.lookup[node.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)