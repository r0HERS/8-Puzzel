import pygame
import sys
import time
import copy

import puzzel8 as puzzel


state = puzzel.state_empty

pygame.init()
size = width, height = 800, 600

black = (0, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
numFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

board = puzzel.initial_state(state)

def draw_board(board):
    tiles = []
    for row in range(len(board)):
        row_tiles = []
        for cell in range(len(board[row])):
            rect = pygame.Rect(tile_origin[0] + cell * tile_size, tile_origin[1] + row * tile_size, tile_size, tile_size)
            pygame.draw.rect(screen, white, rect, 3)
            if board[row][cell] in possible_nums:
                num = numFont.render(str(board[row][cell]), True, green)
            else:
                num = numFont.render(str(board[row][cell]), True, white)

            numRect = num.get_rect()
            numRect.center = rect.center
            screen.blit(num, numRect)

            row_tiles.append(rect)
        tiles.append(row_tiles)
    return tiles

tile_size = 100
tile_origin = (width / 2 - (1.5 * tile_size), height / 2 - (1.5 * tile_size))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(black)

    title = largeFont.render("Play 8 - PUZZLE", True, white)
    titleRect = title.get_rect()
    titleRect.center = ((width / 2), 50)
    screen.blit(title, titleRect)

    possible_nums = puzzel.available_moves(board)

    tiles = draw_board(board)
    
    click, _, _ = pygame.mouse.get_pressed()

    if click == 1:
        mouse = pygame.mouse.get_pos()
        for row in range(len(board)):
            for cell in range(len(board[row])):
                cell_value = board[row][cell]
                if tiles[row][cell].collidepoint(mouse):
                    print(f"Você clicou no número: {cell_value} na posição ({row}, {cell})")
                    time.sleep(0.2)

                    if cell_value in possible_nums:
                        board = puzzel.make_move(board, cell_value)
                        final = puzzel.is_final(board)
                        if final:
                            print("Você completou o puzzle!")
                        break

    pygame.display.flip()
