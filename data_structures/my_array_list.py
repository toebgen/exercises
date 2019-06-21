
class MyArrayList():
    def __init__(self):
        # Instantiate initial fixed size array
        self.size = 1
        self.array = [None] * self.size
        self.index = -1  # Points to last used index in ArrayList
        self.extension_factor = 2


    def extend(self):
        """
        Extend current fixed array size by self.extension_factor.
        Copy saved content over.
        """
        new_size = self.size * self.extension_factor
        new_array = [None] * new_size
        new_array[:self.size] = self.array
        self.array = new_array
        self.size = new_size
        # Don't touch self.index


    def diminish(self):
        """
        Reduce current fixed array size by self.extension_factor.
        """
        if self.size <= 1:
            # Won't diminish further
            return

        new_size = int(self.size / self.extension_factor)
        new_array = self.array[:new_size]
        self.array = new_array
        self.size = new_size
        # Make sure this is pointing inside the current size
        self.index = self.size


    def append(self, value):
        """ Append at the end of array. Extend array size if necessary. """
        # TODO: Don't allow multiple values as parameter

        if (self.index + 1) == self.size:
            # Current array is full -> extend
            self.extend()
        self.array[self.index + 1] = value
        self.index += 1
    

    def pop(self):
        """
        RetRemove and return last element from the array
        """
        if (self.index < 0):
            # ArrayList is empty!
            return None

        last_element = self.array[self.index]
        self.array[self.index] = None
        self.index -= 1

        if self.index <= (self.size / self.extension_factor):
            self.diminish()

        return last_element


    def __getitem__(self, index):
        """ [] operator, return value """
        return self.array[index]
    

    def __len__(self):
        return self.index + 1
    

    def __in__(self, value):
        for val in self.array:
            if val == value:
                return True
        return False
