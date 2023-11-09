from collections import deque

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque()

    def process(self, arrival_time, processing_time):
        # Remove finished processes
        while self.finish_time and self.finish_time[0] <= arrival_time:
            self.finish_time.popleft()

        if len(self.finish_time) < self.size:
            if len(self.finish_time) == 0:
                started_at = arrival_time
            else:
                started_at = max(self.finish_time[-1], arrival_time)
            self.finish_time.append(started_at + processing_time)
            return started_at
        else:
            return -1

def process_packets(buffer_size, n, packets):
    buffer = Buffer(buffer_size)
    result = []

    for arrival_time, processing_time in packets:
        result.append(buffer.process(arrival_time, processing_time))

    return result

def main():
    buffer_size, n = map(int, input().split())
    packets = [list(map(int, input().split())) for _ in range(n)]

    processing_times = process_packets(buffer_size, n, packets)

    for time in processing_times:
        print(time)

if __name__ == "__main__":
    main()
