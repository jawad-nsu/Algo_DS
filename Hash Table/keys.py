class HashTable:
    def __init__(self, size):
        self.data_map = size * [None]

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_hash_table(self):
        for key, val in enumerate(self.data_map):
            print(val)

    def set(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        
        self.data_map[index].append([key, value])

    def get(self, key):
        index = self.__hash(key)
        if self.data_map[index] != None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        
        return None

    def keys(self):
        result = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    result.append(self.data_map[i][j][0])
        return result

    

my_hashtable = HashTable(7)
my_hashtable.print_hash_table()

my_hashtable.set("bolts", 1000)
my_hashtable.set("washers", 1200)
my_hashtable.print_hash_table()

my_hashtable.set("pepper", 1500)
my_hashtable.print_hash_table()

print(my_hashtable.keys())
