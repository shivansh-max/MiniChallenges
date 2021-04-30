import pygame
import random

pygame.init()
pygame.font.init()

# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

# SHAPE FORMATS

S = [['.....',
    '......',
    '..00..',
    '.00...',
    '.....'],
    ['.....',
    '..0..',
    '..00.',
    '...0.',
    '.....']]

Z = [['.....',
    '.....',
    '.00..',
    '..00.',
    '.....'],
    ['.....',
    '..0..',
    '.00..',
    '.0...',
    '.....']]

I = [['..0..',
    '..0..',
    '..0..',
    '..0..',
    '.....'],
    ['.....',
    '0000.',
    '.....',
    '.....',
    '.....']]

O = [['.....',
    '.....',
    '.00..',
    '.00..',
    '.....']]

J = [['.....',
    '.0...',
    '.000.',
    '.....',
    '.....'],
    ['.....',
    '..00.',
    '..0..',
    '..0..',
    '.....'],
    ['.....',
    '.....',
    '.000.',
    '...0.',
    '.....'],
    ['.....',
    '..0..',
    '..0..',
    '.00..',
    '.....']]

L = [['.....',
    '...0.',
    '.000.',
    '.....',
    '.....'],
    ['.....',
    '..0..',
    '..0..',
    '..00.',
    '.....'],
    ['.....',
    '.....',
    '.000.',
    '.0...',
    '.....'],
    ['.....',
    '.00..',
    '..0..',
    '..0..',
    '.....']]

T = [['.....',
    '..0..',
    '.000.',
    '.....',
    '.....'],
    ['.....',
    '..0..',
    '..00.',
    '..0..',
    '.....'],
    ['.....',
    '.....',
    '.000.',
    '..0..',
    '.....'],
    ['.....',
    '..0..',
    '.00..',
    '..0..',
    '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape

# only class
class Piece(object):
    def __init__(self,x,y,shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

# functions (what they do is straight forward  (names))
def create_grid(locked_pos={}):
    grid = [[(0,0,0)for x in range(10)] for x in range(20)]
    for i in range(len(grid)):
        for j in range(len[i]):
            if (i,j) in locked_pos:
                c = locked_pos[(j,i)]
                grid[i] [j] = c
    return grid

def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation%shape.shape]
    for i, line in enumerate(format):
        row = list(line)
        for j in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))
    for i,pos in enumerate(positions):
        positions[i] = (pos[1] -2, pos[2] - 4)

    return positions


def valid_space(shape, grid):
    accepted = [[(j,i)for j in range(10) if grid[i][j] == (0, 0, 0)]for i in range(20)]
    accepted = [j for sub in accepted for j in sub]
    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted:
            if pos[1] > -1:
                return false

    return true

def check_lost(positions):
    for pos in positions:
        x,y = pos
        if y < 1:
            return True

    return False


def get_shape():
    return Piece(5, 0, random.choice(shapes))


def draw_text_middle(text, size, color, surface):
    pass


def draw_grid(surface, row, col, grid):
    sx = top_left_x
    sy = top_left_y
    for i in range(len(grid)):
        pygame.draw.line(surface,(255,255,255),(sx,sy+i*blocksze), (sx+play_width, sy+i*block_size))
        for j in ragne(len(grid[i])):
            pygame.draw.line(surface, (255, 255, 255), (sx + j * blocksze, sy), (sx + j * blocksze , sy+play_height))



def clear_rows(grid, locked):
    pass

def draw_next_shape(shape, surface):
    pass

def draw_window(surface,grid):
    surface.fill((0, 0, 0))

    pygame.font.init()
    font = pygame.font.SysFont('comoicsans', 60)
    label = font.render("TETRIS", 1, (255, 255, 255))

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width / 2), 30))

    for i in range(grid):
        for j in range(grid[i]):
            pygame.draw.rect(surface, grid[i] [j], (top_left_x + j*block_size, top_left_y + i*block_size,block_size,block_size),0)

    pygame.draw(surface, (255 , 0 , 0), (top_left_x,top_left_y),4)
    pygame.display.update()


def main(win):
    # variables
    locked_position = {}
    grid = create_grid(locked_position)
    changepiece = False
    run = true
    current_peice = get_shape()
    next_peice = get_shape()
    time = pygame.time.Clock()
    fall_time = 0
    false_speed = 0.27
    while run:
        grid = create_grid(locked_position)
        fall_time += clock.get_rawtime
        clock.tick()

        if fall_time/1000 > false_speed:
            fall_time = 0
            current_peice.y += 1
            if not (valid_space(current_peice, grid)) and current_peice.y > 0:
                current_peice -= 1
                changepeice = True


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = false
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    current_peice.x -= 1
                    if not(valid_space(current_peice, grid)):
                        current_peice += 1
                if event.key == K_RIGHT:
                    current_peice.x += 1
                    if not(valid_space(current_peice, grid)):
                        current_peice += 1
                if event.key == K_DOWN:
                    current_peice.x += 1
                    if not(valid_space(current_peice, grid)):
                        current_peice.y += 1
                if event.key == K_UP:
                    current_peice.rotation +=  1
                    if not(valid_space(current_peice, grid)):
                        current_peice += 1
        shape_pos = convert_shape_format(current_peice)
        for i in range(len(shape_pos)):
            x,y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_peice.color

        if changepeice:
            for pos in shape_pos:
                p = (pos[0],pos[1])
                locked_position[p] = current_peice.color
            current_peice = next_peice
            next_peice = get_shape()
            changepeice = False

        if check_lost(locked_position):
            run = False
        draw_window(win,grid)

    pygame.display.quit()
def main_menu(win):
    main(win)

# make the screen
win = pygame.display.set_mode((s_width,s_height))
pygame.display.set_caption("TETTRIS @SHIVANSH...")
main_menu(win)  # start game
