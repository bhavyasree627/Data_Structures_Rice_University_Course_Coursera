class DisjointSet:
    def __init__(self, sizes):
        self.parent = list(range(len(sizes)))
        self.rank = [0] * len(sizes)
        self.sizes = sizes
        self.max_size = max(sizes)

    def find(self, table):
        if table != self.parent[table]:
            self.parent[table] = self.find(self.parent[table])
        return self.parent[table]

    def merge(self, destination, source):
        real_destination, real_source = self.find(destination), self.find(source)

        if real_destination == real_source:
            return

        if self.rank[real_destination] > self.rank[real_source]:
            self.parent[real_source] = real_destination
            self.sizes[real_destination] += self.sizes[real_source]
            self.sizes[real_source] = 0
            self.max_size = max(self.max_size, self.sizes[real_destination])
        else:
            self.parent[real_destination] = real_source
            self.sizes[real_source] += self.sizes[real_destination]
            self.sizes[real_destination] = 0
            self.max_size = max(self.max_size, self.sizes[real_source])

            if self.rank[real_destination] == self.rank[real_source]:
                self.rank[real_source] += 1

    def get_max_size(self):
        return self.max_size

# Read input
n, m = map(int, input().split())
table_sizes = list(map(int, input().split()))

# Initialize Disjoint Set
ds = DisjointSet(table_sizes)
li=[]
# Process merge queries
for _ in range(m):
    destination, source = map(int, input().split())
    ds.merge(destination - 1, source - 1)
    li.append(ds.get_max_size())
for i in li:
    print(i)
