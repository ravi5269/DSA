class Array:
    def __init__(self):
        self.array = []

    def special_create(self, elements):
        self.array = elements

    def create(self, value):
        self.array.append(value)

    def update(self, index, value):
        if 0 <= index < len(self.array):
            self.array[index] = value
        else:
            print("Index out of bounds")

    def delete(self, index):
        if 0 <= index < len(self.array):
            del self.array[index]
        else:
            print("Index out of bounds")

    def remove(self, value):
        if value in self.array:
            self.array.remove(value)
        else:
            print("Value not found in array")

    def insert(self, index, value):
        if 0 <= index <= len(self.array):
            self.array.insert(index, value)
        else:
            print("Index out of bounds")

    def select(self, index):
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            print("Index out of bounds")
            return None

    def display(self):
        print(self.array)

# Example usage
dynamic_array = Array()

# Special create
dynamic_array.special_create([1, 2, 3, 4, 5])
dynamic_array.display()  # Output: [1, 2, 3, 4, 5]

# Create
dynamic_array.create(6)
dynamic_array.display()  # Output: [1, 2, 3, 4, 5, 6]

# Update
dynamic_array.update(2, 10)
dynamic_array.display()  # Output: [1, 2, 10, 4, 5, 6]

# Delete
dynamic_array.delete(1)
dynamic_array.display()  # Output: [1, 10, 4, 5, 6]

# Remove
dynamic_array.remove(4)
dynamic_array.display()  # Output: [1, 10, 5, 6]
# Delete
dynamic_array.delete(1)
dynamic_array.display()  # Output: [1, 10, 4, 5, 6]

# Remove
dynamic_array.remove(4)
dynamic_array.display()  # Output: [1, 10, 5, 6]

# Insert
dynamic_array.insert(1, 20)
dynamic_array.display()  # Output: [1, 20, 10, 5, 6]

# Select
print(dynamic_array.select(3))  # Output: 5

# Trying to update with an out of bounds index
dynamic_array.update(10, 100)  # Output: Index out of bounds

# Trying to delete with an out of bounds index
dynamic_array.delete(10)  # Output: Index out of bounds

# Trying to remove a value not in the array
dynamic_array.remove(100)  # Output: Value not found in array

# Trying to insert with an out of bounds index
dynamic_array.insert(10, 100)  # Output: Index out of bounds

# Trying to select with an out of bounds index
print(dynamic_array.select(10))  # Output: Index out of bounds, None

# Insert
dynamic_array.insert(1, 20)
dynamic_array.display()  # Output: [1, 20, 10, 5, 6]

# Select
print(dynamic_array.select(3))  # Output: 5

# Trying to update with an out of bounds index
dynamic_array.update(10, 100)  # Output: Index out of bounds

# Trying to delete with an out of bounds index
dynamic_array.delete(10)  # Output: Index out of bounds

# Trying to remove a value not in the array
dynamic_array.remove(100)  # Output: Value not found in array

# Trying to insert with an out of bounds index
dynamic_array.insert(10, 100)  # Output: Index out of bounds

# Trying to select with an out of bounds index
print(dynamic_array.select(10))  # Output: Index out of bounds, None
