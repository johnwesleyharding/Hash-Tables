class HashTableEntry:

    def __init__(self, key, value):
        
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    
    def __init__(self, capacity):
        
        self.prime = 1099511628211
        self.offset = 14695981039346656037
        self.capacity = capacity
        self.storage = [None] * self.capacity

    def fnv1(self, key):

        hash_bytes = key.encode()
        total = self.offset
    
        for b in hash_bytes:
            
            total *= self.prime
            total ^= b
            total &= 0xffffffffffffffff
            
        return total

    def djb2(self, key):

        pass

    def hash_index(self, key):

        return self.fnv1(key) % self.capacity

    def put(self, key, value):
        
        index = self.hash_index(key)
        
        if self.storage[index] == None or self.storage[index].key == key:
            
            self.storage[index] = HashTableEntry(key, value)
        
        else:

            node = self.storage[index]
                
            while node.next != None and node.next.key != key:

                node = node.next

            node.next = HashTableEntry(key, value)

    def delete(self, key):
        
        index = self.hash_index(key)
        node = self.storage[index]
        
        if node == None:
            
            return 'Key not found'
        
        if node.key == key:
            
            if node.next != None:
                
                self.storage[index] = node.next
                
            else:
                
                self.storage[index] = None
        
        else:
            
            while node.key != key and node.next != None:
                
                prev = node
                node = node.next
                
            if node.key == key:
                
                prev.next = node.next
                node = None
                
            else:
                
                return 'Key not found'

    def get(self, key):
        
        index = self.hash_index(key)
        node = self.storage[index]
        
        if node != None:
            
            while node.key != key and node.next != None:
                
                node = node.next
                
            if node.key == key:
                
                return node.value

    def resize(self):
        
        storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity
        
        for entry in storage:
            
            if entry != None:
                
                self.put(entry.key, entry.value)
                
                while entry.next != None:
                    
                    entry = entry.next
                    self.put(entry.key, entry.value)
                
if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
