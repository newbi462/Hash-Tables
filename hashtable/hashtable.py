from doubly_linked_list import DoublyLinkedList

class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, size):
        self.capacity = size # How many slots the hash table has
        # SIZE because of "ht = HashTable(0x10000)" from test file
        # self.capacity because hash_i) already set this value

        self.hash_table = [None] * self.capacity # Space to hold values

        self.count = 0


    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash = 5381 # Why 5381? Because it’s prime, and it works pretty well
        for x in key:
            hash = (( hash << 5) + hash) + ord(x) # << 5, like 33 is optmsation for older CPUs
        return hash & 0xffffffff # because 32 bit

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity # because I filled in djb2()

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        #index = hash_index(key)
        #hash_table[index] = value
        #### self.hash_table[self.hash_index(key)] = value
        #Find the hash index
        if self.hash_table[self.hash_index(key)] is None:
            self.hash_table[self.hash_index(key)] = DoublyLinkedList()
            self.hash_table[self.hash_index(key)].add_to_head( [key, value] )
            self.count += 1
        else: #Search the list for the key
            if self.hash_table[self.hash_index(key)].find_and_replace(key, value) is None:
                #If it's there, replace the value
                pass
            else:
                #If it's not, append a new record to the list
                self.hash_table[self.hash_index(key)].add_to_tail( [key, value] )
                self.count += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        #index = hash_index(key)
        #hash_table[index] = None
        ###self.hash_table[self.hash_index(key)] = None
        #Find the hash index
        if self.hash_table[self.hash_index(key)] is None:
            return None
        else: #Search the list for the key
            if self.hash_table[self.hash_index(key)].find_for_del(key) is None:
                return None
            else:
                node_to_del = self.hash_table[self.hash_index(key)].find_for_del(key)
                self.hash_table[self.hash_index(key)].delete(node_to_del)
                self.count -= 1


        #If found, delete the node from the list, (return the node or value?)
        #Else return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        #index = hash_index(key)
        #return hash_table[index]
        ###return self.hash_table[self.hash_index(key)]
        #Find the hash index
        if self.hash_table[self.hash_index(key)] is None:
            return None
        else: #Search the list for the key
            return self.hash_table[self.hash_index(key)].find_for_get(key)
        #If found, return the value
        #Else return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """


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
