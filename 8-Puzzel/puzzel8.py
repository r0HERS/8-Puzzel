import random
import copy

EMPTY = 'X'

state_empty = [[EMPTY,EMPTY,EMPTY],
        [EMPTY,EMPTY,EMPTY],
        [EMPTY,EMPTY,EMPTY]]

actions = ["up","down","left","right"]

def initial_state(state):
    
    nums = [1,2,3,4,5,6,7,8,EMPTY]
    
    random.shuffle(nums)

    i = 0

    for row in range(len(state)):
        for cell in range(len(state[row])):
            state[row][cell] = nums[i]
            i += 1
    
    return state

def print_state(state):
    for row in state:
        print(row)

def is_final(state):

    final = [[1,2,3],
             [4,5,6],
             [7,8,EMPTY]]
    
    for row in range(len(state)):
        for cell in range(len(state[row])):
            if state[row][cell] != final[row][cell]:
                return False

    return True


def chose_action(state):

    numbers = available_moves(state)

    print("Células possiveis de mover:")
    print(numbers)
    
    cell = int(input("Escolha uma destas celulas:"))

    while cell not in numbers:
        cell = int(input("Escolha uma destas celulas:"))
    


    return cell
    
    
def available_moves(state):

    empty_location = None

    numbers = []
    
    for row in range(len(state)):
        for cell in range(len(state[row])):
            if state[row][cell] == EMPTY:
                empty_location = (row, cell)
                break
    
    if empty_location[0]-1 != -1:
        numbers.append(state[empty_location[0]-1][empty_location[1]])
    if empty_location[0]-1 != 1:
        numbers.append(state[empty_location[0]+1][empty_location[1]])
    if empty_location[1]-1 != -1:
        numbers.append(state[empty_location[0]][empty_location[1]-1])
    if empty_location[1]-1 != 1:
        numbers.append(state[empty_location[0]][empty_location[1]+1])

    return numbers

def make_move(state,number):

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

    return  copy_state


'''def play(state):
    
    if is_final(state):
        print_state(start_state)
        return 0
    
    print_state(start_state)

    final = False
    number = chose_action(state)
    new_state = make_move(state,number)
    final = is_final(state)
    print_state(new_state)

    while final != True:
        number = chose_action(new_state)
        new_state = make_move(new_state,number)
        final = is_final(new_state)
        print_state(new_state)
    return 0 

start_state = initial_state(state_empty)
play(start_state)'''

