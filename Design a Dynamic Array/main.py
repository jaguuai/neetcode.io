class DynamicArray:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        self.capacity = capacity
        self.size = 0
        self.array = [0] * capacity

    def get(self, i):
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[i]

    def set(self, i, n):
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        self.array[i] = n

    def pushback(self, n):
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1

    def popback(self):
        if self.size == 0:
            raise IndexError("Pop from empty array")
        value = self.array[self.size - 1]
        self.size -= 1
        return value

    def resize(self):
        new_capacity = self.capacity * 2
        new_array = [0] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def getSize(self):
        return self.size

    def getCapacity(self):
        return self.capacity

# Example usage:
# Create a dynamic array with an initial capacity of 1
array = DynamicArray(1)

# Get the size of the array (should be 0 initially)
print(array.getSize())  # Output: 0

# Get the capacity of the array (should be 1 initially)
print(array.getCapacity())  # Output: 1

# Push elements to the array
array.pushback(1)
print(array.getCapacity())  # Output: 1
array.pushback(2)  # This will trigger a resize
print(array.getCapacity())  # Output: 2

# Get the size and capacity after pushing elements
print(array.getSize())  # Output: 2
print(array.getCapacity())  # Output: 2

# Get and set elements
print(array.get(0))  # Output: 1
print(array.get(1))  # Output: 2
array.set(1, 3)
print(array.get(1))  # Output: 3

# Pop an element from the end
print(array.popback())  # Output: 3
print(array.getSize())  # Output: 1
print(array.getCapacity())  # Output: 2