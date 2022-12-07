class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None
        print("add New Node", data)