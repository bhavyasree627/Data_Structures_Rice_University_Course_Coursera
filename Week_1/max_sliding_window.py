from collections import deque

def max_sliding_window(arr, m):
    n = len(arr)
    max_values = []

    # Initialize a deque to store indices of elements in the current window
    window = deque()

    # Process the first window
    for i in range(m):
        while window and arr[i] >= arr[window[-1]]:
            window.pop()
        window.append(i)

    max_values.append(arr[window[0]])

    # Process the remaining windows
    for i in range(m, n):
        while window and window[0] <= i - m:
            window.popleft()

        while window and arr[i] >= arr[window[-1]]:
            window.pop()

        window.append(i)
        max_values.append(arr[window[0]])

    return max_values

# Input
n = int(input())
arr = list(map(int, input().split()))
m = int(input())

# Calculate maximum values in sliding windows
result = max_sliding_window(arr, m)

# Output
print(" ".join(map(str, result)))
