class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cacheMap = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cacheMap:
            return -1
        
        # Remove existing
        thisNode = self.cacheMap[key]
        self.removeSelf(thisNode)
        
        ## Update Tail
        self.updateTail(thisNode)
        
        return thisNode.val

    def removeSelf(self, thisNode):     
        thisNode.prev.next = thisNode.next
        thisNode.next.prev = thisNode.prev

    def updateTail(self, thisNode):
        self.tail.prev.next = thisNode
        thisNode.prev = self.tail.prev
        thisNode.next = self.tail
        self.tail.prev = thisNode

    def put(self, key: int, value: int) -> None:
        
        newNode = Node(key, value)
        
        # If new
        if key in self.cacheMap:
           ## Remove existing node
            curr = self.cacheMap[key]
            self.removeSelf(curr)

        ## Update Tail
        self.updateTail(newNode)

        ## Update Map
        self.cacheMap[key] = newNode

        # If exceeding capacity
        if len(self.cacheMap) > self.capacity:
            d = self.head.next.key
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            del self.cacheMap[d]
