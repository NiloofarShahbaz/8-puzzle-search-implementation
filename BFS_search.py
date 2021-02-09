import timeit
from datetime import datetime
from queue import Queue
from puzzle import Puzzle
import time
import numpy as np




def breadth_first_search(initial_state, thread_number=1):
    start_node = Puzzle(initial_state, None, None, 0)
    if start_node.goal_test():
        return start_node.find_solution()
    q = Queue()
    q.put(start_node)

    q_temp = Queue()
    explored = []
    i = 0
    total_steps = 0
    total_time = np.float64(0)
    threads_list_times = []


    while not (q.empty()):
        t0 = time.process_time()
        i += 1
        node = q.get()
        explored.append(node.state)
        children = node.generate_child()
        for child in children:
            if child.state not in explored:
                q_temp.put(child)

        t1 = time.process_time()
        diff = t1 - t0
        threads_list_times.append(diff)

        if i == thread_number or q.empty():
            total_time += max(threads_list_times)
            threads_list_times = []
            i = 0
            total_steps += 1

            while not q_temp.empty():
                curr_node = q_temp.get()
                if curr_node.goal_test():
                    return total_time, curr_node.find_solution(), total_steps
                q.put(curr_node)
    return
