from queue import PriorityQueue
from puzzle import Puzzle


def astar(initial_state):
    count = 0
    visited = []
    start_node = Puzzle(initial_state,None,None,0)

    # Create priority queue
    q = PriorityQueue()

    # Insert initial state
    q.put((start_node.evaluation_function,count,start_node))


    while not q.empty():
        # Get the state with the lowest f(n)
        node = q.get()
        node = node[2]

        # Mark the state visited
        visited.append(node.state)

        # Check if current state is goal state
        if node.goal_test():
            return node.find_solution()
        
        # Generate child and insert to pqueue
        children = node.generate_child()
        for child in children:
            if child.state not in visited:
                count += 1
                q.put((child.evaluation_function,count,child))
    return

