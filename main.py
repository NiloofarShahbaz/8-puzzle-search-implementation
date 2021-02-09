from time import time
from BFS_search import breadth_first_search
from Astar_search import Astar_search
from RBFS_search import recursive_best_first_search
from puzzle import Puzzle
import numpy as np

state=[[1, 3, 4,
        8, 6, 2,
        7, 0, 5],

       [2, 8, 1,
        0, 4, 3,
        7, 6, 5],

       [2, 8, 1,
        4, 6, 3,
        0, 7, 5]]

print('BFS')
for i in range(0, 3):
    print('------------------------------------------')
    for k in [1,1] + list(range(1,20)):
        all_times = []
        for j in range(1000):
            Puzzle.num_of_instances = 0
            total_time, solution, total_steps = breadth_first_search(state[i], k)
            all_times.append(total_time)
        print(
            f"K = {k} | space : {Puzzle.num_of_instances} | total time : {np.average(all_times)} | "
            f"total steps : {total_steps} | solution depth : {len(solution)} ")

print(' ')
print('A star')
for i in range(0, 3):
    print('------------------------------------------')
    for k in [1,1] + list(range(1,20)):
        all_times = []
        for j in range(100):
            Puzzle.num_of_instances = 0
            total_time, solution, total_steps = Astar_search(state[i], k)
            all_times.append(total_time)
        print(
            f"K = {k} | space : {Puzzle.num_of_instances} | total time : {np.average(all_times)} | "
            f"total steps : {total_steps} | solution depth : {len(solution)} ")

