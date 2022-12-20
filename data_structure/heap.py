class Heap(object):
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def node_up(self, i):
        while (i // 2) > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i//2], self.heap_list[i] = self.heap_list[i], self.heap_list[i//2]
            i = i // 2

    def node_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.find_min_child(i)
            if self.heap_list[mc] < self.heap_list[i]:
                self.heap_list[mc], self.heap_list[i] = self.heap_list[i], self.heap_list[mc]
            i = mc        

    def find_min_child(self, i):
        if (i * 2 + 1) > self.current_size:
            return i * 2
        if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
            return i * 2 + 1
        else:
            return i * 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.node_up(self.current_size)

    def del_min_node(self):
        self.heap_list[0], self.heap_list[-1] = self.heap_list[-1], self.heap_list[0]
        self.heap_list.pop()

        self.node_down(0)       

    def build_heap(self, alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist

        while (i > 0):
            self.node_down(i)
            i -= 1