import pygame
import sys
import time
from collections import deque

import puzzle8 as puzzle

state = puzzle.state_empty

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

def draw_board(board):
    screen.fill(black)  # Limpa a tela antes de desenhar
    tiles = []
    for row in range(len(board)):
        row_tiles = []
        for cell in range(len(board[row])):
            rect = pygame.Rect(tile_origin[0] + cell * tile_size, tile_origin[1] + row * tile_size, tile_size, tile_size)
            pygame.draw.rect(screen, white, rect, 3)
            if board[row][cell] != 0:
                if board[row][cell] in puzzle.available_moves(board):
                    num = numFont.render(str(board[row][cell]), True, green)
                elif board[row][cell] == puzzle.state_final[row][cell] and board[row][cell] not in puzzle.available_moves(board):
                    num = numFont.render(str(board[row][cell]), True, blue)
                else:
                    num = numFont.render(str(board[row][cell]), True, white)

                numRect = num.get_rect()
                numRect.center = rect.center
                screen.blit(num, numRect)

            row_tiles.append(rect)
        tiles.append(row_tiles)
    pygame.display.flip()  # Atualiza a tela após desenhar o tabuleiro
    return tiles

def bfs_generator(initial_board):
    queue = deque([initial_board])
    visited = set()
    visited.add(puzzle.state_to_tuple(initial_board))

    while queue:
        current_state = queue.popleft()

        if puzzle.is_final(current_state):
            yield current_state, True
            return

        for neighbor in puzzle.get_neightboors(current_state):
            neighbor_tuple = puzzle.state_to_tuple(neighbor)
            if neighbor_tuple not in visited:
                queue.append(neighbor)
                visited.add(neighbor_tuple)
        
        yield current_state, False

def greedy_generator(initial_board):
    queue = deque([initial_board])
    visited = set()
    visited.add(puzzle.state_to_tuple(initial_board))

    while queue:
        current_board = queue.popleft()
        manhattan_value = float('inf')
        next_state = None

        if puzzle.is_final(current_board):
            yield current_board, True
            return

        for neighbor in puzzle.get_neightboors(current_board):
            if puzzle.state_to_tuple(neighbor) not in visited:
                x = puzzle.manhattan(neighbor)
                if x < manhattan_value:
                    manhattan_value = x
                    next_state = neighbor

        if next_state is None:
            next_state = puzzle.make_random_move(current_board,1)  # Evita erro se nenhum next_state válido for encontrado
        
        queue.append(next_state)
        visited.add(puzzle.state_to_tuple(next_state))

        yield current_board, False  # Pausa a execução e retorna o estado atual

board = puzzle.initial_state(100)
tile_size = 100
tile_origin = (width / 2 - (1.5 * tile_size), height / 2 - (1.5 * tile_size))

count = 0
game_over = False
mode = None
current_board = board
bfs_steps = None
greedy_steps = None

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

        playNormalButton = pygame.Rect((width / 10), (height / 2), width / 4, 50)
        playNormal = mediumFont.render("On your own", True, black)
        playNormalRect = playNormal.get_rect()
        playNormalRect.center = playNormalButton.center
        pygame.draw.rect(screen, white, playNormalButton)
        screen.blit(playNormal, playNormalRect)

        playAIButton = pygame.Rect(4 * (width / 10), (height / 2), width / 4, 50)
        playAI = mediumFont.render("IA BFS", True, black)
        playAIRect = playAI.get_rect()
        playAIRect.center = playAIButton.center
        pygame.draw.rect(screen, white, playAIButton)
        screen.blit(playAI, playAIRect)

        playAIGreedyButton = pygame.Rect(7 * (width / 10), (height / 2), width / 4, 50)
        playAIGreedy = mediumFont.render("IA Greedy", True, black)
        playAIGreedyRect = playAIGreedy.get_rect()
        playAIGreedyRect.center = playAIGreedyButton.center
        pygame.draw.rect(screen, white, playAIGreedyButton)
        screen.blit(playAIGreedy, playAIGreedyRect)

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
                bfs_steps = bfs_generator(current_board)
            elif playAIGreedyButton.collidepoint(mouse):
                time.sleep(0.2)
                mode = 2
                greedy_steps = greedy_generator(current_board)

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
            possible_nums = puzzle.available_moves(board)
            tiles = draw_board(board)
            
            click, _, _ = pygame.mouse.get_pressed()

            if click == 1:
                mouse = pygame.mouse.get_pos()
                for row in range(len(board)):
                    for cell in range(len(board[row])):
                        cell_value = board[row][cell]
                        if tiles[row][cell].collidepoint(mouse):
                            time.sleep(0.2)

                            if cell_value in possible_nums:
                                board = puzzle.make_move(board, cell_value)
                                final = puzzle.is_final(board)
                                count += 1
                                if final:
                                    game_over = True
                                break
        else:
            tiles = draw_board(puzzle.state_final)
            
            congrats_text = largeFont.render("Parabéns! Você completou o puzzle!", True, green)
            congratsRect = congrats_text.get_rect()
            congratsRect.center = (width / 2, height - 100) 
            screen.blit(congrats_text, congratsRect)

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
                    board = puzzle.initial_state(100)
                    mode = None

        pygame.display.flip()
        
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
                    current_board, game_over = next(bfs_steps)
                    tiles = draw_board(current_board)
                    count += 1
                    if game_over:
                        bfs_steps = None
                except StopIteration:
                    bfs_steps = None
        else:
            tiles = draw_board(puzzle.state_final)
            
            congrats_text = largeFont.render(f"AI Resolveu o problema em {count} lances!", True, green)
            congratsRect = congrats_text.get_rect()
            congratsRect.center = (width / 2, height - 100) 
            screen.blit(congrats_text, congratsRect)

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
                    board = puzzle.initial_state(100)
                    current_board = board
                    mode = None

        pygame.display.flip()

    elif mode == 2:
        screen.fill(black)

        title = largeFont.render("8 - PUZZLE  Greedy AI", True, white)
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
                    current_board, game_over = next(greedy_steps)
                    tiles = draw_board(current_board)
                    count += 1
                    time.sleep(0.5)
                    if game_over:
                        greedy_steps = None
                except StopIteration:
                    greedy_steps = None
        else:
            tiles = draw_board(puzzle.state_final)
            
            congrats_text = largeFont.render(f"AI Resolveu o problema em {count} lances!", True, green)
            congratsRect = congrats_text.get_rect()
            congratsRect.center = (width / 2, height - 100) 
            screen.blit(congrats_text, congratsRect)

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
                    board = puzzle.initial_state(100)
                    current_board = board
                    mode = None

        pygame.display.flip()
