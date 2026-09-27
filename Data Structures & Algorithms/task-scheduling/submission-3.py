from collections import Counter, deque
from typing import List
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        def approach_1():
            counter = Counter(tasks)
            max_heap = []
            for key, value in counter.items():
                heapq.heappush(max_heap, (-value, key))

            queue = deque()
            time = 0
            while max_heap or queue:
                time += 1
                print(time, max_heap, queue)
                # if not max_heap:
                #     break
                processed_queue = False
                if queue:
                    if queue:
                        # print(f"QUEUE - {queue[0][2]}")
                        # break
                        if queue[0][2] < time:
                            processed_queue = True
                            # print(processed_queue)
                            (key, value, curr_time) = queue.popleft()
                            if value + 1 < 0:
                                # heapq.heappush(max_heap, (popped[1]+1, popped[0]))
                                queue.append((key, value + 1, time + n))
                        else:
                            pass
                            # print(f"IDLE at Time = {time}")

                if not processed_queue and max_heap:
                    print("Processing Heap Element...")
                    (value, key) = heapq.heappop(max_heap)
                    if value + 1 < 0:
                        queue.append((key, value + 1, time + n))

            return time

        def approach_2():
            counter = Counter(tasks)
            max_heap = []
            for key, value in counter.items():
                heapq.heappush(max_heap, (-value, key))

            queue = deque()
            time = 0
            while max_heap or queue:
                time += 1
                print(time, max_heap, queue)
                if queue:
                    if queue[0][2] < time:
                        (key, value, curr_time) = queue.popleft()
                        heapq.heappush(max_heap, (value, key))
                if max_heap:
                    print("Processing Heap Element...")
                    (value, key) = heapq.heappop(max_heap)
                    if value + 1 < 0:
                        queue.append((key, value + 1, time + n))
                else:
                    print("IDLE")
            return time

        return approach_2()





tasks=["A","A","A","B","B","B","C","C","C","D","D","E"]
n=2
print(Solution().leastInterval(tasks, n))