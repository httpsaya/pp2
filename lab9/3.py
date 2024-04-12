import pygame
import sys
import math

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

# Drawing settings
drawing_color = BLACK
drawing_tool = "pencil"
brush_size = 5
eraser_size = 20
drawing = False
last_pos = None

# Create a surface for drawing
draw_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
draw_surface.fill(WHITE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                drawing_tool = "rectangle"
            elif event.key == pygame.K_t:
                drawing_tool = "circle"
            elif event.key == pygame.K_e:
                drawing_tool = "eraser"
            elif event.key == pygame.K_s:
                drawing_color = RED
            elif event.key == pygame.K_g:
                drawing_color = GREEN
            elif event.key == pygame.K_b:
                drawing_color = BLUE
            elif event.key == pygame.K_1:
                drawing_tool = "square"
            elif event.key == pygame.K_2:
                drawing_tool = "right_triangle"
            elif event.key == pygame.K_3:
                drawing_tool = "equilateral_triangle"
            elif event.key == pygame.K_4:
                drawing_tool = "rhombus"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                last_pos = None
        elif event.type == pygame.MOUSEMOTION:
            if drawing and last_pos is not None:
                if drawing_tool == "rectangle":
                    pygame.draw.rect(draw_surface, drawing_color, (last_pos, (event.pos[0] - last_pos[0], event.pos[1] - last_pos[1])))
                elif drawing_tool == "circle":
                    radius = max(abs(event.pos[0] - last_pos[0]), abs(event.pos[1] - last_pos[1]))
                    pygame.draw.circle(draw_surface, drawing_color, last_pos, radius, brush_size)
                elif drawing_tool == "eraser":
                    pygame.draw.circle(draw_surface, WHITE, event.pos, eraser_size)
                elif drawing_tool == "square":
                    side_length = min(abs(event.pos[0] - last_pos[0]), abs(event.pos[1] - last_pos[1]))
                    square_end = (last_pos[0] + side_length, last_pos[1] + side_length)
                    pygame.draw.rect(draw_surface, drawing_color, (last_pos, (side_length, side_length)))
                elif drawing_tool == "right_triangle":
                    pygame.draw.polygon(draw_surface, drawing_color, [(last_pos[0], last_pos[1]), (last_pos[0], event.pos[1]), (event.pos[0], event.pos[1])])
                elif drawing_tool == "equilateral_triangle":
                    triangle_height = abs(event.pos[0] - last_pos[0])
                    triangle_end = (last_pos[0] + triangle_height, last_pos[1] + triangle_height)
                    pygame.draw.polygon(draw_surface, drawing_color, [(last_pos[0], last_pos[1]), (last_pos[0], triangle_end[1]), (triangle_end[0], triangle_end[1])])
                elif drawing_tool == "rhombus":
                    rhombus_width = abs(event.pos[0] - last_pos[0])
                    rhombus_height = abs(event.pos[1] - last_pos[1])
                    pygame.draw.polygon(draw_surface, drawing_color, [(last_pos[0], last_pos[1] + rhombus_height // 2), (last_pos[0] + rhombus_width // 2, last_pos[1]), (last_pos[0] + rhombus_width, last_pos[1] + rhombus_height // 2), (last_pos[0] + rhombus_width // 2, last_pos[1] + rhombus_height)])

    screen.fill(WHITE)
    screen.blit(draw_surface, (0, 0))

    # Draw tool selection
    pygame.draw.rect(screen, BLACK, (0, 0, 50, 200))
    pygame.draw.rect(screen, drawing_color, (10, 10, 30, 30))
    pygame.draw.rect(screen, BLACK, (0, 200, 50, 200))
    pygame.draw.rect(screen, RED, (10, 210, 30, 30))
    pygame.draw.rect(screen, GREEN, (10, 250, 30, 30))
    pygame.draw.rect(screen, BLUE, (10, 290, 30, 30))

    if drawing_tool == "rectangle":
        pygame.draw.rect(screen, BLACK, (5, 5, 40, 40), 2)
    elif drawing_tool == "circle":
        pygame.draw.circle(screen, BLACK, (25, 25), 20, 2)
    elif drawing_tool == "eraser":
        pygame.draw.circle(screen, BLACK, (25, 25), 10, 2)

    # Обновление экрана
    pygame.display.flip()
    clock.tick(FPS)
