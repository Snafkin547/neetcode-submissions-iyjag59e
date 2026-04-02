class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        # Limit
        self.limit = capacity
        # Determine if key exists
        self.keys = defaultdict(lambda: Node(0, 0))
        # Actual storage
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def append(self,  node) -> None:
        # Weave the current to the end
        self.tail.prev.next, node.prev = node, self.tail.prev
        node.next, self.tail.prev = self.tail, node

    def skip(self, node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1

        # Get the value
        node = self.keys[key]
        
        # Skip the current node and append the node to recent
        self.skip(node)
        self.append(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            node = self.keys[key]
            node.val = value
            # Skip the current node and append the node to recent
            self.skip(node)
            self.append(node)

        else:
            node = Node(key, value)
            self.keys[key] = node
            self.append(node)
            if len(self.keys) > self.limit:
                print(self.head.next.val)
                del self.keys[self.head.next.key]
                self.skip(self.head.next)
