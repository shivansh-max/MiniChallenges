# Imports
import pygame
import sys

# Init
pygame.init()

# Global Vars
Width = 1000
Height = 700
playerH = 100
playerW = 20
size = (Width, Height)

# Rgb
light_blue = (3, 252, 227)
green = (3, 135, 45)
yellow = (255, 247, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
white = (255,255,255)
red = (255,0,0)

# Win
win = pygame.display.set_mode(size)


def main(Surface):

	gameover = False

	x1 = 0
	y1 = 0
	x2 = Width - playerW
	y2 = 0

	while not(gameover):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			y1 -= 2

		if keys[pygame.K_s]:
			y1 += 2

		if keys[pygame.K_UP]:
			y2 -= 2
		if keys[pygame.K_DOWN]:
			y2 += 2        
        
		if y1 < 0:
			y1 = 0

		if y1 > Height - playerH:
			y1 = Height - playerH

		if y2 < 0:
			y2 = 0

		if y2 > Height - playerH:
			y2 = Height - playerH

		win.fill(black)		
		
		player_left_rect = pygame.Rect( x1, y1, playerW, playerH)
		player_right_rect = pygame.Rect( x2, y2, playerW, playerH)

		player_left = pygame.draw.rect(Surface, red, ( x1, y1, playerW, playerH))
		player_right = pygame.draw.rect(Surface, blue, player_right_rect)

		pygame.display.update()


main(win)

