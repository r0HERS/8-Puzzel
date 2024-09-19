import random
import copy
from collections import deque
import heapq
import time


EMPTY = 0

state_final = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, EMPTY]]

def initial_state(n):
    state = State(copy.deepcopy(state_final))  

    for i in range(n):
        numbers = state.available_moves() 
        k = random.choice(numbers)
        state = state.make_move(k)  

    return state.state

class State():
    def __init__(self, state=None, step_count=0,previous = None):
        self.state = state
        self.step_count = step_count
        self.previous = previous

    def print_state(self):
        for row in self.state:
            print(row)
        print()

    def is_final(self):
        for row in range(len(self.state)):
            for cell in range(len(self.state[row])):
                if self.state[row][cell] != state_final[row][cell]:
                    return False
        return True

    def state_to_tuple(self):
        return tuple(tuple(row) for row in self.state)

    def available_moves(self):
        empty_location = None
        numbers = []

        for row in range(len(self.state)):
            for cell in range(len(self.state[row])):
                if self.state[row][cell] == EMPTY:
                    empty_location = (row, cell)
                    break

        if empty_location[0] - 1 != -1:
            numbers.append(self.state[empty_location[0] - 1][empty_location[1]])
        if empty_location[0] + 1 != 3:
            numbers.append(self.state[empty_location[0] + 1][empty_location[1]])
        if empty_location[1] - 1 != -1:
            numbers.append(self.state[empty_location[0]][empty_location[1] - 1])
        if empty_location[1] + 1 != 3:
            numbers.append(self.state[empty_location[0]][empty_location[1] + 1])

        return numbers

    def make_move(self, number):
        empty_location = None
        number_location = None
        copy_state = copy.deepcopy(self.state)

        for row in range(len(self.state)):
            for cell in range(len(self.state[row])):
                if self.state[row][cell] == EMPTY:
                    empty_location = (row, cell)
                    break

        for row in range(len(self.state)):
            for cell in range(len(self.state[row])):
                if self.state[row][cell] == number:
                    number_location = (row, cell)
                    break

        copy_state[empty_location[0]][empty_location[1]] = number
        copy_state[number_location[0]][number_location[1]] = EMPTY

        return State(copy_state, self.step_count + 1,previous=self)

    def get_neighbors(self):
        neighbors = []
        for number in self.available_moves():
            next_state = self.make_move(number)
            neighbors.append(next_state)
        return neighbors

    def manhattan(self):
        value = 0
        for row in range(len(self.state)):
            for cell in range(len(self.state[row])):
                num = self.state[row][cell]
                if num != EMPTY:
                    for i in range(len(state_final)):
                        for j in range(len(state_final[i])):
                            if state_final[i][j] == num:
                                value += abs(row - i) + abs(cell - j)
        return value

    def A_star(self):
        new_count = self.step_count + 1
        manhattan_value = self.manhattan()
        total_value = new_count + manhattan_value

        print(total_value)
        print(new_count)
        print(manhattan_value)

        return (total_value, new_count, self)

    def reconstruct_path(self):
        path = []
        current = self
        while current:
            path.append(current)
            current = current.previous
        return path[::-1]

class BFS():
    def __init__(self):
        self.queue = deque()

    def add_to_structure(self, state):
        self.queue.append(state)

    def get_from_structure(self):
        return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0


class DFS():
    def __init__(self):
        self.stack = []

    def add_to_structure(self, state):
        self.stack.append(state)

    def get_from_structure(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

class Greedy():
    
    pass

class Astar():
    def __init__(self):
        self.priority_queue = []
        self.counter = 0  

    def add_to_structure(self, state):
        total = state.A_star()
        heapq.heappush(self.priority_queue, (total[0], self.counter, total[2]))
        self.counter += 1

    def get_from_structure(self):
        return heapq.heappop(self.priority_queue)[2]

    def is_empty(self):
        return len(self.priority_queue) == 0


def playIA(algorithm, state):
    start_time = time.time()
    structure = algorithm()

    visited = set()
    structure.add_to_structure(state)
    visited.add(state.state_to_tuple())

    steps = 0
    while not structure.is_empty():
        steps += 1
        current_state = structure.get_from_structure()

        if current_state.is_final():
            print("Solução encontrada!")
            current_state.print_state()
            path = current_state.reconstruct_path()  
            print(len(path))
            #time.sleep(10)
            for state_in_path in path:
                state_in_path.print_state()
            print(f"Número de passos: {steps}")
            print(f"Tempo de execução: {time.time() - start_time:.2f} segundos")
            return

        for neighbor in current_state.get_neighbors():
            if neighbor.state_to_tuple() not in visited:
                structure.add_to_structure(neighbor)
                visited.add(neighbor.state_to_tuple())

        current_state.print_state()

    print("Solução não encontrada.")

initial__state = State(initial_state(100))
#playIA(BFS, initial__state)

#playIA(DFS, initial__state)

playIA(Astar, initial__state)