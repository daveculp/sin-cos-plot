import pygame
import time
import math

# Some config width height settings
canvas_width = 1280
canvas_height = 960

# Just define some colors we can use
GREEN = pygame.Color(0, 255, 0, 0)
RED = pygame.Color(255,0,0,0)
BLUE = pygame.Color(0,0,255)
background_color = pygame.Color(0, 0, 0, 0)

pygame.init()
# Set the window title
pygame.display.set_caption("Sine Wave")

# Make a screen to see
screen = pygame.display.set_mode((canvas_width, canvas_height))
screen.fill(background_color)

# Make a surface to draw on
surface = pygame.Surface((canvas_width, canvas_height))
surface.fill(background_color)

# Simple main loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Redraw the background
	surface.fill(background_color)

	# Update sine wave
	sin_frequency = 4
	sin_amplitude = 50 # in px
	sin_speed = 1
	
	cos_frequency = 4
	cos_amplitude = 50 # in px
	cos_speed = 1
	for x in range(0, canvas_width):
		y = int((canvas_height/2) + sin_amplitude*math.sin(sin_frequency*((float(x)/canvas_width)*(2*math.pi) + (sin_speed*time.time()))))
		y2 = int((canvas_height/2) + cos_amplitude*math.cos(cos_frequency*((float(x)/canvas_width)*(2*math.pi) + (cos_speed*time.time()))))
		surface.set_at((x, y), GREEN)
		surface.set_at((x, y2), RED)
	# Put the surface we draw on, onto the screen
	screen.blit(surface, (0, 0))

	# Show it.
	pygame.display.flip()
