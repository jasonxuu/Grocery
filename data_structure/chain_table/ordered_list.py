from node import Node

class OrderList(Node):
    def __init__(self):
        self.head = None

    def add(self, data):
        temp = Node(data)
        current = self.head
        previous = None
        stop = False
        while (current != None):
            if current.get_data() > data:
                stop = True
                break
            previous = current
            current = current.get_next()

        if stop:
            temp.set_next(current)
            previous.set_next(temp)
        else:
            temp.set_next(self.head)
            self.head = temp

    def search(self, data):
        current = self.head
        while (current != None):
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()
        return False