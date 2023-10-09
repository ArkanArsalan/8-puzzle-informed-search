class Puzzle:
    goal_state = [1,2,3,4,5,6,7,8,0]
    heuristic = None
    evaluation_function = None
    num_of_instances = 0

    def __init__(self,state,parent,action,path_cost):
        # Initialiaze parent, state, and action
        self.parent = parent
        self.state = state
        self.action = action

        # Calculate path cost to the root
        if parent:
            self.path_cost = parent.path_cost + path_cost
        else:
            self.path_cost = path_cost

        # Heuristic function
        self.manhattan_distance()

        # Evaluation_function = heuristic function + path cost 
        self.evaluation_function = self.heuristic+self.path_cost

        Puzzle.num_of_instances += 1

    def __str__(self):
        return str(self.state[0:3])+'\n'+str(self.state[3:6])+'\n'+str(self.state[6:9])
    
    # Heuristic function (manhattan distance)
    def manhattan_distance(self):
        self.heuristic = 0
        for num in range(1,9):
            distance = abs(self.state.index(num) - self.goal_state.index(num))
            i = int(distance/3)
            j = int(distance%3)
            self.heuristic = self.heuristic+i+j

    def wrong_placement(self):
        self.heuristic = 0
        for num in range(1,8):
            if (num != self.state.index(num - 1)) :
                self.heuristic += 1


    # Test current state to goal state
    def goal_test(self):
        if self.state == self.goal_state:
            return True
        return False

    @staticmethod
    def find_possible_action(i,j):
        legal_action = ['U', 'D', 'L', 'R']
        # Empty place is at the top side
        if i == 0:  
            # Up move is disable
            legal_action.remove('U')
        # Empty place is at the bottom
        elif i == 2:  
            # Down move is disable
            legal_action.remove('D')
        # Empty place is at left side
        if j == 0:
            # Left move is disable
            legal_action.remove('L')
        # Empty place is at right side
        elif j == 2:
            # Right move is disbale
            legal_action.remove('R')
        return legal_action

    # Generate all possible child at given state
    def generate_child(self):
        children = []
        # Find position of the empty space
        x = self.state.index(0)
        i = int(x / 3)
        j = int(x % 3)
        # Find all legal action/move
        legal_actions = self.find_possible_action(i,j)

        # For every action create a new children state
        for action in legal_actions:
            new_state = self.state.copy()
            if action == 'U':
                new_state[x], new_state[x-3] = new_state[x-3], new_state[x]
            elif action == 'D':
                new_state[x], new_state[x+3] = new_state[x+3], new_state[x]
            elif action == 'L':
                new_state[x], new_state[x-1] = new_state[x-1], new_state[x]
            elif action == 'R':
                new_state[x], new_state[x+1] = new_state[x+1], new_state[x]
            children.append(Puzzle(new_state,self,action,1))
        return children

    # Generate solution path
    def find_solution(self):
        solution = []
        solution.append(self.action)
        path = self
        while path.parent !=  None:
            path = path.parent
            solution.append(path.action)
        solution = solution[:-1]
        solution.reverse()
        return solution
