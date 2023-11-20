class HashTable:
    def __init__(self, num_buckets):
        self.num_buckets = num_buckets
        self.buckets = [[] for _ in range(num_buckets)]

    def hash_function(self, string):
        p = 1000000007
        x = 263
        hash_value = 0
        for i, char in enumerate(string):
            hash_value = (hash_value + ord(char) * x**i) % p
        return hash_value % self.num_buckets

    def add(self, string):
        hash_value = self.hash_function(string)
        if string not in self.buckets[hash_value]:
            self.buckets[hash_value].insert(0, string)

    def del_string(self, string):
        hash_value = self.hash_function(string)
        if string in self.buckets[hash_value]:
            self.buckets[hash_value].remove(string)

    def find(self, string):
        hash_value = self.hash_function(string)
        return string in self.buckets[hash_value]

    def check(self, index):
        if index < 0 or index >= self.num_buckets:
            print()
        else:
            for item in self.buckets[index]:
                print(item, end=' ')
            print()

if __name__ == '__main__':
    num_buckets = int(input())
    num_queries = int(input())

    hash_table = HashTable(num_buckets)

    for _ in range(num_queries):
        query = input()
        if query.startswith('add'):
            string = query[4:]
            hash_table.add(string)
        elif query.startswith('del'):
            string = query[4:]
            hash_table.del_string(string)
        elif query.startswith('find'):
            string = query[5:]
            if hash_table.find(string):
                print('yes')
            else:
                print('no')
        elif query.startswith('check'):
            index = int(query[6:])
            hash_table.check(index)
