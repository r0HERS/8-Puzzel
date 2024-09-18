import random
import copy
from collections import deque
import math
import heapq

EMPTY = 0

state_empty = [[EMPTY, EMPTY, EMPTY],
               [EMPTY, EMPTY, EMPTY],
               [EMPTY, EMPTY, EMPTY]]

state_final = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, EMPTY]]


def initial_state(n):
    state = copy.deepcopy(state_final)

    for i in range(n):
        numbers = available_moves(state)
        k = random.choice(numbers)
        state = make_move(state, k)

    return state

def make_random_move(state,n):

    for i in range(n):
        numbers = available_moves(state)
        k = random.choice(numbers)
        state = make_move(state, k)

    return state


def print_state(state):
    for row in state:
        print(row)


def is_final(state):
    for row in range(len(state)):
        for cell in range(len(state[row])):
            if state[row][cell] != state_final[row][cell]:
                return False

    return True


def available_moves(state):
    empty_location = None

    numbers = []

    for row in range(len(state)):
        for cell in range(len(state[row])):
            if state[row][cell] == EMPTY:
                empty_location = (row, cell)
                break

    if empty_location[0] - 1 != -1:
        numbers.append(state[empty_location[0] - 1][empty_location[1]])
    if empty_location[0] + 1 != 3:
        numbers.append(state[empty_location[0] + 1][empty_location[1]])
    if empty_location[1] - 1 != -1:
        numbers.append(state[empty_location[0]][empty_location[1] - 1])
    if empty_location[1] + 1 != 3:
        numbers.append(state[empty_location[0]][empty_location[1] + 1])

    return numbers


def make_move(state, number):
    empty_location = None
    number_location = None
    copy_state = copy.deepcopy(state)

    for row in range(len(state)):
        for cell in range(len(state[row])):
            if state[row][cell] == EMPTY:
                empty_location = (row, cell)
                break

    for row in range(len(state)):
        for cell in range(len(state[row])):
            if state[row][cell] == number:
                number_location = (row, cell)
                break

    copy_state[empty_location[0]][empty_location[1]] = number
    copy_state[number_location[0]][number_location[1]] = EMPTY

    return copy_state


def get_neightbors(state):
    neightbors = []

    for number in available_moves(state):
        next_state = make_move(state, number)
        neightbors.append(next_state)

    return neightbors


def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def manhattan(state):
    value = 0
    for row in range(len(state)):
        for cell in range(len(state[row])):
            num = state[row][cell]
            if num != EMPTY:  
                for i in range(len(state_final)):
                    for j in range(len(state_final[i])):
                        if state_final[i][j] == num:
                            value += abs(row - i) + abs(cell - j)
    return value


##################

#  BFS, DFS, A*  #

##################

class BFS:

    def search(initial_board):
        print("Executando BFS ")

        queue = deque([initial_board])
        visited = set()
        visited.add(state_to_tuple(initial_board))

        while queue:
            current_state = queue.popleft()

            if is_final(current_state):
                yield current_state, True
                return

            for neighbor in get_neightbors(current_state):
                neighbor_tuple = state_to_tuple(neighbor)
                if neighbor_tuple not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor_tuple)
            
            yield current_state, False



class DFS:

    def search(initial_board):
        print("Executando DFS ")
        stack = [initial_board]
        visited = set()
        visited.add(state_to_tuple(initial_board))

        while stack:
            current_state = stack.pop()

            if is_final(current_state):
                yield current_state, True
                return

            for neighbor in get_neightbors(current_state):
                neighbor_tuple = state_to_tuple(neighbor)
                if neighbor_tuple not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor_tuple)
            
            yield current_state, False



class Astar:

    def search(initial_board):
        print("Executando A* ")
        visited = set()
        priority_queue = []
        step_count = 0
        
        # Estado inicial com manhattan_value
        manhattan_value = manhattan(initial_board)
        heapq.heappush(priority_queue, (manhattan_value + step_count, step_count, initial_board))
        visited.add(state_to_tuple(initial_board))

        while priority_queue:
            current_state = heapq.heappop(priority_queue)

            # Verifica se é o estado final
            if is_final(current_state[2]):
                yield current_state[2], True
                return

            # Explora os vizinhos
            for neighbor in get_neightbors(current_state[2]):
                if state_to_tuple(neighbor) not in visited:
                    visited.add(state_to_tuple(neighbor))
                    # Calcula o valor total (f = g + h)
                    tuple_state = A_star(neighbor, current_state[1])
                    heapq.heappush(priority_queue, tuple_state)
            
            yield current_state[2], False





'''def playIA():
    state = initial_state(100)

    visited = set()
    queue = deque([state])
    next_state = state_empty
    visited.add(state_to_tuple(state))

    while queue:
        current_state = queue.popleft()
        manhattan_value = 100
        if is_final(current_state):
            print("achoooooooooooooooooo")
            print_state(current_state)
            return 0
        
        for neightbor in get_neightbors(current_state):
            if state_to_tuple(neightbor) not in visited:
                x = manhattan(neightbor)
                if x < manhattan_value:
                    manhattan_value = x
                    print(manhattan_value)
                    next_state = neightbor

        if next_state == current_state:
            next_state = initial_state(1) 
                
        queue.append(next_state)
        visited.add(state_to_tuple(next_state))

        print_state(current_state)
    return None


playIA()'''


def A_star(state,step_count):

    new_count = step_count + 1

    manhattan_value = manhattan(state)

    toltal_value = new_count + manhattan_value 

    return (toltal_value,new_count,state)


'''def playIAStar():
    state = initial_state(100)

    visited = set()

    priority_queue = []

    step_count = 0 

    manhattan_value = manhattan(state)

    heapq.heappush(priority_queue,(manhattan_value + step_count,step_count,state))


    while priority_queue:
        
        current_state = heapq.heappop(priority_queue)
        print_state(current_state[2])
        print(current_state[0])
        print(current_state[1])
        if is_final(current_state[2]):
            print("achoooooooooooooooooooooooooooooo")
            print_state(current_state[2])
            return 0

        for neighbor in get_neightbors(current_state[2]):
            if state_to_tuple(neighbor) not in visited:
                visited.add(state_to_tuple(neighbor))
                tuple_state = A_star(neighbor, current_state[1])
                heapq.heappush(priority_queue, tuple_state)

    return

playIAStar()'''