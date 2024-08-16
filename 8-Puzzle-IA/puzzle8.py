import random
import copy
from collections import deque

EMPTY = ' '

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


def get_neightboors(state):
    neightbors = []

    for number in available_moves(state):
        next_state = make_move(state, number)
        neightbors.append(next_state)

    return neightbors


def state_to_tuple(state):
    return tuple(tuple(row) for row in state)


'''def playIA():
    state = initial_state(100)

    visited = set()
    queue = deque([state])
    visited.add(state_to_tuple(state))

    while queue:
        current_state = queue.popleft()

        if is_final(current_state):
            print("achoooooooooooooooooo")
            print_state(current_state)
            return 0

        for neightbor in get_neightboors(current_state):
            neighbor_tuple = state_to_tuple(neightbor)
            if neighbor_tuple not in visited:
                queue.append(neightbor)
                visited.add(neighbor_tuple)

        print_state(current_state)
    return None


playIA()'''
