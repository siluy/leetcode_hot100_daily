#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class LRUCache:
    class _Node:
        __slots__ = ("key", "val", "prev", "next")
        def __init__(self, key=0, val=0):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None
            
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = self._Node()
        self.tail = self._Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_first(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _move_to_first(self, node):
        self._remove(node)
        self._add_first(node)

    def _pop_last(self):
        node = self.tail.prev
        self._remove(node)
        return node

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
           return -1
        self._move_to_first(node)
        return node.val 

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node:
            node.val = value
            self._move_to_first(node)
            return
        node = self._Node(key, value)
        self.cache[key] = node
        self._add_first(node)
        if len(self.cache) > self.cap:
            lru = self._pop_last()
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

