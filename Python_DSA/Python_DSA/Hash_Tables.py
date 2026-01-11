'''my_list = []

def hash_function(key):
    sum_of_chars = sum(ord(char) for char in key)
    return sum_of_chars % 10

def add(name):
    index = hash_function(name)
    my_list.append((index, name))
    
def contains(name):
    index = hash_function(name)
    for i, n in my_list:
        if i == index and n == name:
            return True
        return False
    
add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
add('Stuart')
print(my_list)'''

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
            self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
            return None
        
    def delete(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
            return False
    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Index {i}: {bucket}")

ht  = HashTable()
ht.insert("name", "Alice")
ht.insert("age", 30)
ht.insert("city", "New York")
ht.display()
print(ht.search("name"))  # Output: Alice
ht.delete("age")
ht.display()
print(ht.search("age"))  # Output: None
