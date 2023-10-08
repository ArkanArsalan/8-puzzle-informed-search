from time import time
from astar import astar
from rbfs import recursive_best_first_search
from gbfs import gbfs
from puzzle import Puzzle


initial_state =[[1, 2, 5,
                3, 4, 0,
                6, 7, 8]]


Puzzle.num_of_instances = 0
time_start = time()
astar_path = astar(initial_state [0])
time_end = time() - time_start
print('A*:',astar_path)
print('space:', Puzzle.num_of_instances)
print('time:', time_end)
print()

Puzzle.num_of_instances = 0
time_start = time()
gbfs_path = gbfs(initial_state [0])
time_end = time() - time_start
print('GBFS:',gbfs_path)
print('space:', Puzzle.num_of_instances)
print('time:', time_end)
print()

Puzzle.num_of_instances = 0
time_start = time()
RBFS = recursive_best_first_search(initial_state [0])
time_end = time() - time_start
print('RBFS:',RBFS)
print('space:', Puzzle.num_of_instances)
print('time:', time_end)
print()

print('------------------------------------------')