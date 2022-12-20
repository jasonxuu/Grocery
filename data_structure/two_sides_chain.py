from chain_table.node import Node

class Solution:
    def __init__(self, size):
        self.size = size
        self.head = None
        self.tail = None
        self.hash = {}

    def insert_first(self, node):
        #将原本head->node, 调整为new_node -> node
        node.pre = self.head
        node.next = self.head.next
        self.head.next = node
        self.head.pre = node

    def remove_last(self):
        self.hash.pop(self.tail.pre.key)
        self.tail.pre.pre.next = self.tail
        self.tail.pre = self.tail.pre.pre

    def set(self, key, value):
        if key not in self.key_record:
            node = Node(key, val)
            self.hash[key] = node
            if len(self.key_record) > 2:
                self.remove_last()

    def LRU(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        #pre的使用，说明实际上的链表方向是和head一样的。
        self.tail.pre = self.head
        

