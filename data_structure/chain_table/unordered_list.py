from node import Node

class UnOrderedList(Node):
    def __init__(self):
        self.head = None

    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def length(self):
        current = self.head
        ct = 0
        while current:
            ct += 1
            current = current.get_next()

        return ct

    def search(self, data):
        current = self.head
        found = False
        while (current and (not found)):
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, data):
        current = self.head
        found = False
        previous = None 
        while (current and (not found)):
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        
