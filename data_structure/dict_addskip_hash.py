class HashTable(object):
    def __init__(self):
        self.size = 11
        self.skip = 1
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def _hash(self, value):
        return value % self.size

    def _rehash(self, old_value):
        return (old_value + self.skip) % self.size

    def put(self, key, data):
        key_pos = self._hash(key)
        if self.slots[key_pos] == None:
            self.slots[key_pos] = key
            self.data[key_pos] = data
        else:
            if self.slots[key_pos] == key:
                self.data[key_pos] = data
            else:
                next_key_pos = self._rehash(key_pos)
                while (self.slots[next_key_pos] != None) and (self.slots[next_key_pos] != key):
                    next_key_pos = self._rehash(next_key_pos)

                if self.slots[next_key_pos] == None:
                    self.slots[next_key_pos] = key
                self.data[next_key_pos] = data

    def get(self, key):
        key_pos = self._hash(key)
        start_pos = key_pos

        while True:
            if self.slots[key_pos]:
                if self.slots[key_pos] == key:
                    return self.data[key_pos]
                else:
                    key_pos = self._rehash(key_pos)
                    if key_pos == start_pos:
                        return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)