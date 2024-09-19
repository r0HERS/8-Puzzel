import pygame
import sys
import time
from collections import deque
import heapq

import puzzle8 as puzzle 

state = puzzle.initial_state(100)

pygame.init()
size = width, height = 800, 600

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
numFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

def draw_board(state):
    screen.fill(black)  
    board = state.state
    tiles = []
    for row in range(len(board)):
        row_tiles = []
        for cell in range(len(board[row])):
            rect = pygame.Rect(tile_origin[0] + cell * tile_size, tile_origin[1] + row * tile_size, tile_size, tile_size)
            pygame.draw.rect(screen, white, rect, 3)
            if board[row][cell] != 0:
                if board[row][cell] in state.available_moves():
                    num = numFont.render(str(board[row][cell]), True, green)
                elif board[row][cell] == puzzle.state_final[row][cell] and board[row][cell] not in state.available_moves():
                    num = numFont.render(str(board[row][cell]), True, blue)
                else:
                    num = numFont.render(str(board[row][cell]), True, white)

                numRect = num.get_rect()
                numRect.center = rect.center
                screen.blit(num, numRect)

            row_tiles.append(rect)
        tiles.append(row_tiles)
    pygame.display.flip() 
    return tiles

def bfs_generator(initial_state):
    bfs = puzzle.BFS()
    visited = set()
    bfs.add_to_structure(initial_state)
    visited.add(initial_state.state_to_tuple())

    while not bfs.is_empty():
        current_state = bfs.get_from_structure()

        if current_state.is_final():
            yield current_state, True
            return

        for neighbor in current_state.get_neighbors():
            if neighbor.state_to_tuple() not in visited:
                bfs.add_to_structure(neighbor)
                visited.add(neighbor.state_to_tuple())
        
        yield current_state, False

def greedy_generator(initial_state):
    greedy = puzzle.Greedy()
    pass

def dfs_generator(initial_state):
    dfs = puzzle.DFS()
    visited = set()
    dfs.add_to_structure(initial_state)
    visited.add(initial_state.state_to_tuple())

    while not dfs.is_empty():
        current_state = dfs.get_from_structure()

        if current_state.is_final():
            yield current_state, True
            return

        for neighbor in current_state.get_neighbors():
            if neighbor.state_to_tuple() not in visited:
                dfs.add_to_structure(neighbor)
                visited.add(neighbor.state_to_tuple())
        
        yield current_state, False

def astar_generator(initial_state):
    astar = puzzle.Astar()
    visited = set()
    astar.add_to_structure(initial_state)
    visited.add(initial_state.state_to_tuple())

    while not astar.is_empty():
        current_state = astar.get_from_structure()

        if current_state.is_final():
            yield current_state, True
            return

        for neighbor in current_state.get_neighbors():
            if neighbor.state_to_tuple() not in visited:
                astar.add_to_structure(neighbor)
                visited.add(neighbor.state_to_tuple())
        
        yield current_state, False

board = puzzle.State(puzzle.initial_state(100))  
tile_size = 100
tile_origin = (width / 2 - (1.5 * tile_size), height / 2 - (1.5 * tile_size))

count = 0
game_over = False
mode = None
current_state = board
bfs_steps = None
greedy_steps = None
dfs_steps = None
astar_steps = None

start_time = 0  
resolution_time = 0  
shortest_path_length = 0  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if mode is None:
        screen.fill(black)
        
        title = largeFont.render("Play 8 - PUZZLE", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        button_width = width / 4
        button_height = 50
        button_y = height / 2 - 60  

        playNormalButton = pygame.Rect((width / 10), button_y, button_width, button_height)
        playNormal = mediumFont.render("On your own", True, black)
        playNormalRect = playNormal.get_rect()
        playNormalRect.center = playNormalButton.center
        pygame.draw.rect(screen, white, playNormalButton)
        screen.blit(playNormal, playNormalRect)

        playAIButton = pygame.Rect(4 * (width / 10), button_y, button_width, button_height)
        playAI = mediumFont.render("IA BFS", True, black)
        playAIRect = playAI.get_rect()
        playAIRect.center = playAIButton.center
        pygame.draw.rect(screen, white, playAIButton)
        screen.blit(playAI, playAIRect)

        playAIGreedyButton = pygame.Rect(7 * (width / 10), button_y, button_width, button_height)
        playAIGreedy = mediumFont.render("IA Greedy", True, black)
        playAIGreedyRect = playAIGreedy.get_rect()
        playAIGreedyRect.center = playAIGreedyButton.center
        pygame.draw.rect(screen, white, playAIGreedyButton)
        screen.blit(playAIGreedy, playAIGreedyRect)

        playAIDFSButton = pygame.Rect((width / 10), button_y + 80, button_width, button_height)
        playAIDFS = mediumFont.render("IA DFS", True, black)
        playAIDFSRect = playAIDFS.get_rect()
        playAIDFSRect.center = playAIDFSButton.center
        pygame.draw.rect(screen, white, playAIDFSButton)
        screen.blit(playAIDFS, playAIDFSRect)

        playAIAStarButton = pygame.Rect(7 * (width / 10), button_y + 80, button_width, button_height)
        playAIAStar = mediumFont.render("IA A*", True, black)
        playAIAStarRect = playAIAStar.get_rect()
        playAIAStarRect.center = playAIAStarButton.center
        pygame.draw.rect(screen, white, playAIAStarButton)
        screen.blit(playAIAStar, playAIAStarRect)

        pygame.display.flip()

        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playNormalButton.collidepoint(mouse):
                time.sleep(0.2)
                mode = 1
            elif playAIButton.collidepoint(mouse):
                time.sleep(0.2)
                mode = 0
                bfs_steps = bfs_generator(current_state)
                start_time = time.time()  
            elif playAIDFSButton.collidepoint(mouse):
                time.sleep(0.2)
                mode = 3
                dfs_steps = dfs_generator(current_state)
                start_time = time.time()  
            elif playAIGreedyButton.collidepoint(mouse):
                time.sleep(0.2)
                mode = 2
                greedy_steps = greedy_generator(current_state)
                start_time = time.time()  
            elif playAIAStarButton.collidepoint(mouse):
                time.sleep(0.2)
                mode = 4
                astar_steps = astar_generator(current_state)
                start_time = time.time() 


    elif mode == 0:  
        screen.fill(black)

        title = largeFont.render("8 - PUZZLE AI", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        moves_count = largeFont.render(f"Moves: {count}", True, white)
        moves_countRect = moves_count.get_rect()
        moves_countRect.center = ((width / 2), 100)
        screen.blit(moves_count, moves_countRect)

        if not game_over:
            if bfs_steps is not None:
                try:
                    current_state, game_over = next(bfs_steps)
                    tiles = draw_board(current_state)
                    count += 1
                    if game_over:
                        bfs_steps = None
                        resolution_time = time.time() - start_time  
                        shortest_path_length = len(current_state.reconstruct_path())  
                except StopIteration:
                    bfs_steps = None
        else:
            tiles = draw_board(puzzle.State(puzzle.state_final))

            congrats_text = largeFont.render(f"AI Resolveu o problema em {count} lances!", True, green)
            congratsRect = congrats_text.get_rect()
            congratsRect.center = (width / 2, height - 100)
            screen.blit(congrats_text, congratsRect)

            resolution_time_text = mediumFont.render(f"Tempo de resolução: {resolution_time:.2f} segundos", True, white)
            resolution_time_rect = resolution_time_text.get_rect()
            resolution_time_rect.center = (width / 2, 50)
            screen.blit(resolution_time_text, resolution_time_rect)

            shortest_path_text = mediumFont.render(f"Tamanho do caminho: {shortest_path_length} movimentos", True, white)
            shortest_path_rect = shortest_path_text.get_rect()
            shortest_path_rect.center = (width / 2, 100)
            screen.blit(shortest_path_text, shortest_path_rect)

            restart_button = mediumFont.render("Recomeçar", True, white)
            restartRect = restart_button.get_rect()
            restartRect.center = (width / 2, height - 50)
            pygame.draw.rect(screen, blue, restartRect.inflate(20, 20), border_radius=10)
            screen.blit(restart_button, restartRect)

            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if restartRect.collidepoint(mouse):
                    game_over = False
                    count = 0
                    current_state = puzzle.State(puzzle.initial_state(100))
                    mode = None

        pygame.display.flip()

    elif mode == 1:  
        screen.fill(black)

        title = largeFont.render("Play 8 - PUZZLE", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        moves_count = largeFont.render(f"Moves: {count}", True, white)
        moves_countRect = moves_count.get_rect()
        moves_countRect.center = ((width / 2), 100)
        screen.blit(moves_count, moves_countRect)

        if not game_over:
            possible_nums = current_state.available_moves()  
            tiles = draw_board(current_state)

            click, _, _ = pygame.mouse.get_pressed()

            if click == 1:
                mouse = pygame.mouse.get_pos()
                for row in range(len(current_state.state)):
                    for cell in range(len(current_state.state[row])):
                        cell_value = current_state.state[row][cell]
                        if tiles[row][cell].collidepoint(mouse):
                            time.sleep(0.2)

                            if cell_value in possible_nums:
                                current_state = current_state.make_move(cell_value)
                                count += 1
                                if current_state.is_final():
                                    game_over = True
                                    resolution_time = time.time() - start_time  
                            break
        else:
            tiles = draw_board(puzzle.State(puzzle.state_final))  

            congrats_text = largeFont.render("Parabéns! Você completou o puzzle!", True, green)
            congratsRect = congrats_text.get_rect()
            congratsRect.center = (width / 2, height - 100)
            screen.blit(congrats_text, congratsRect)

            moves_count_text = mediumFont.render(f"Número de lances: {count} movimentos", True, white)
            moves_count_rect = moves_count_text.get_rect()
            moves_count_rect.center = (width / 2, 100)
            screen.blit(moves_count_text, moves_count_rect)

            restart_button = mediumFont.render("Recomeçar", True, white)
            restartRect = restart_button.get_rect()
            restartRect.center = (width / 2, height - 50)
            pygame.draw.rect(screen, blue, restartRect.inflate(20, 20), border_radius=10)
            screen.blit(restart_button, restartRect)

            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if restartRect.collidepoint(mouse):
                    game_over = False
                    count = 0
                    current_state = puzzle.State(puzzle.initial_state(100))  
                    start_time = time.time()  
                    mode = None

        pygame.display.flip()

    elif mode == 2:  
        screen.fill(black)

        title = largeFont.render("8 - PUZZLE Greedy AI", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        moves_count = largeFont.render(f"Moves: {count}", True, white)
        moves_countRect = moves_count.get_rect()
        moves_countRect.center = ((width / 2), 100)
        screen.blit(moves_count, moves_countRect)

        if not game_over:
            if greedy_steps is not None:
                try:
                    current_state, game_over = next(greedy_steps)
                    tiles = draw_board(current_state)
                    count += 1
                    if game_over:
                        greedy_steps = None
                        resolution_time = time.time() - start_time 
                        shortest_path_length = len(current_state.reconstruct_path())  
                except StopIteration:
                    greedy_steps = None
        else:
            tiles = draw_board(puzzle.State(puzzle.state_final))

            congrats_text = largeFont.render(f"AI Resolveu o problema em {count} lances!", True, green)
            congratsRect = congrats_text.get_rect()
            congratsRect.center = (width / 2, height - 100)
            screen.blit(congrats_text, congratsRect)

            resolution_time_text = mediumFont.render(f"Tempo de resolução: {resolution_time:.2f} segundos", True, white)
            resolution_time_rect = resolution_time_text.get_rect()
            resolution_time_rect.center = (width / 2, 50)
            screen.blit(resolution_time_text, resolution_time_rect)

            shortest_path_text = mediumFont.render(f"Tamanho do caminho: {shortest_path_length} movimentos", True, white)
            shortest_path_rect = shortest_path_text.get_rect()
            shortest_path_rect.center = (width / 2, 100)
            screen.blit(shortest_path_text, shortest_path_rect)

            restart_button = mediumFont.render("Recomeçar", True, white)
            restartRect = restart_button.get_rect()
            restartRect.center = (width / 2, height - 50)
            pygame.draw.rect(screen, blue, restartRect.inflate(20, 20), border_radius=10)
            screen.blit(restart_button, restartRect)

            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if restartRect.collidepoint(mouse):
                    game_over = False
                    count = 0
                    current_state = puzzle.State(puzzle.initial_state(100))
                    mode = None

        pygame.display.flip()

    elif mode == 3: 
        screen.fill(black)

        title = largeFont.render("8 - PUZZLE DFS AI", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        moves_count = largeFont.render(f"Moves: {count}", True, white)
        moves_countRect = moves_count.get_rect()
        moves_countRect.center = ((width / 2), 100)
        screen.blit(moves_count, moves_countRect)

        if not game_over:
            if dfs_steps is not None:
                try:
                    current_state, game_over = next(dfs_steps)
                    tiles = draw_board(current_state)
                    count += 1
                    if game_over:
                        dfs_steps = None
                        resolution_time = time.time() - start_time  
                        shortest_path_length = len(current_state.reconstruct_path())  
                except StopIteration:
                    dfs_steps = None
        else:
            tiles = draw_board(puzzle.State(puzzle.state_final))

            congrats_text = largeFont.render(f"AI Resolveu o problema em {count} lances!", True, green)
            congratsRect = congrats_text.get_rect()
            congratsRect.center = (width / 2, height - 100)
            screen.blit(congrats_text, congratsRect)

            resolution_time_text = mediumFont.render(f"Tempo de resolução: {resolution_time:.2f} segundos", True, white)
            resolution_time_rect = resolution_time_text.get_rect()
            resolution_time_rect.center = (width / 2, 50)
            screen.blit(resolution_time_text, resolution_time_rect)

            shortest_path_text = mediumFont.render(f"Tamanho do caminho: {shortest_path_length} movimentos", True, white)
            shortest_path_rect = shortest_path_text.get_rect()
            shortest_path_rect.center = (width / 2, 100)
            screen.blit(shortest_path_text, shortest_path_rect)

            restart_button = mediumFont.render("Recomeçar", True, white)
            restartRect = restart_button.get_rect()
            restartRect.center = (width / 2, height - 50)
            pygame.draw.rect(screen, blue, restartRect.inflate(20, 20), border_radius=10)
            screen.blit(restart_button, restartRect)

            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if restartRect.collidepoint(mouse):
                    game_over = False
                    count = 0
                    current_state = puzzle.State(puzzle.initial_state(100))
                    dfs_steps = None
                    mode = None

        pygame.display.flip()

    elif mode == 4:  # A*
        screen.fill(black)

        title = largeFont.render("8 - PUZZLE A* AI", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        moves_count = largeFont.render(f"Moves: {count}", True, white)
        moves_countRect = moves_count.get_rect()
        moves_countRect.center = ((width / 2), 100)
        screen.blit(moves_count, moves_countRect)

        if not game_over:
            if astar_steps is not None:
                try:
                    current_state, game_over = next(astar_steps)
                    tiles = draw_board(current_state)
                    count += 1
                    if game_over:
                        astar_steps = None
                        resolution_time = time.time() - start_time  
                        shortest_path_length = len(current_state.reconstruct_path()) 
                except StopIteration:
                    astar_steps = None
        else:
            tiles = draw_board(puzzle.State(puzzle.state_final))

            congrats_text = largeFont.render(f"AI Resolveu o problema em {count} lances!", True, green)
            congratsRect = congrats_text.get_rect()
            congratsRect.center = (width / 2, height - 100)
            screen.blit(congrats_text, congratsRect)

            resolution_time_text = mediumFont.render(f"Tempo de resolução: {resolution_time:.2f} segundos", True, white)
            resolution_time_rect = resolution_time_text.get_rect()
            resolution_time_rect.center = (width / 2, 50)
            screen.blit(resolution_time_text, resolution_time_rect)

            shortest_path_text = mediumFont.render(f"Tamanho do caminho: {shortest_path_length} movimentos", True, white)
            shortest_path_rect = shortest_path_text.get_rect()
            shortest_path_rect.center = (width / 2, 100)
            screen.blit(shortest_path_text, shortest_path_rect)

            restart_button = mediumFont.render("Recomeçar", True, white)
            restartRect = restart_button.get_rect()
            restartRect.center = (width / 2, height - 50)
            pygame.draw.rect(screen, blue, restartRect.inflate(20, 20), border_radius=10)
            screen.blit(restart_button, restartRect)

            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if restartRect.collidepoint(mouse):
                    game_over = False
                    count = 0
                    current_state = puzzle.State(puzzle.initial_state(100))
                    astar_steps = None
                    mode = None

        pygame.display.flip()
