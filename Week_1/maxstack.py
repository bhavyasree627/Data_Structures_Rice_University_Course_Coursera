class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        popped = self.stack.pop()
        if popped == self.max_stack[-1]:
            self.max_stack.pop()
        return popped

    def max(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]

def process_queries(queries):
    stack = MaxStack()
    results = []
    for query in queries:
        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            results.append(stack.max())
    return results

# Take input from console
q = int(input())
queries = []
for _ in range(q):
    query = input().split()
    queries.append(query)

output = process_queries(queries)
for result in output:
    if result is not None:
        print(result)
