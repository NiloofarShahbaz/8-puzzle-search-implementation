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

for i in range(0,1):
    for k in range(1,50):
        all_times = []
        for j in range(1000):
            Puzzle.num_of_instances = 0
            total_time, solution, total_steps = breadth_first_search(state[i], k)
            all_times.append(total_time)
        print(f"K = {k} | space : {Puzzle.num_of_instances} | total time : {np.average(all_times)} | total steps : {total_steps}")
    #
    # Puzzle.num_of_instances = 0
    # t0 = time()
    # astar = Astar_search(state[i])
    # t1 = time() - t0
    # print('A*:',astar)
    # print('space:', Puzzle.num_of_instances)
    # print('time:', t1)
    # print()
    #
    # Puzzle.num_of_instances = 0
    # t0 = time()
    # RBFS = recursive_best_first_search(state[i])
    # t1 = time() - t0
    # print('RBFS:',RBFS)
    # print('space:', Puzzle.num_of_instances)
    # print('time:', t1)
    # print()

    print('------------------------------------------')