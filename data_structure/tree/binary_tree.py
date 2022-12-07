#!/usr/env/python
#coding=utf-8

from tree_node import Node

class BinaryTree(Node):

    def insert_left(self, data):
        if self.left == None:
           self.left = data
        else:
            n = Node(data)
            n.left = self.left
            self.left = n

    def insert_right(self, data):
        if self.right == None:
            self.right = data
        else:
            n = Node(data)
            n.right = self.right
            self.right = n

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_root_val(self, data):
        self.data = data
    
    def get_root_val(self):
        return self.data