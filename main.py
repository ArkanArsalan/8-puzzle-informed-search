from time import time
from astar import astar
from gbfs import gbfs
from puzzle import Puzzle


initial_state =[[7, 2, 4,
                5, 0, 6,
                8, 3, 1]]


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


print('------------------------------------------')