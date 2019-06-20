
class MyHashMap():
    def __init__(self, *args, **kwargs):
        # Instantiate initial fixed size array
        self.array_length = 32
        self.array = [None] * self.array_length
        self.num_saved_elements = 0

        return super().__init__(*args, **kwargs)
    

    def key2index(self, key):
        """ Use simple hash function key->index for now """
        return key % self.array_length


    def insert(self, key, value):
        """
        Insert value at corresponding index to key to the map.
        Always save the given key as well, in order to be able to resolve collisions.
        """

        index = self.key2index(key)
        if self.array[index] == None:
            self.array[index] = [(key, value)]
        else:
            self.array[index].append((key, value))
        self.num_saved_elements += 1
        # print('fill_ratio():', self.fill_ratio())
    

    def __getitem__(self, key):
        """ [key] operator, return value """
        index = self.key2index(key)
        bucket = self.array[index]
        if bucket != None:
            for (_key, _value) in bucket:
                if _key == key:
                    return _value
        raise KeyError('Key not found in HashMap!')
    

    def fill_ratio(self):
        return float(self.num_saved_elements / self.array_length)
