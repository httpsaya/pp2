import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

snake_speed = 15
snake_block = 10
snake_list = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
snake_length = 1
direction = 'RIGHT'

score = 0
level = 1
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

food_active = False
food_position = (0, 0)
food_weight = 1
food_timer = pygame.time.get_ticks()  # Initialize the timer

def generate_food():
    global food_active, food_position, food_weight, food_timer
    food_active = True
    food_position = (random.randint(0, SCREEN_WIDTH // snake_block - 1) * snake_block,
                     random.randint(0, SCREEN_HEIGHT // snake_block - 1) * snake_block)
    food_weight = random.randint(1, 5)  # Random weight (1 to 5)
    food_timer = pygame.time.get_ticks()  # Reset the timer

def check_collision(snake_list, snake_block, screen_width, screen_height):
    head_x, head_y = snake_list[-1]

    if head_x >= screen_width or head_x < 0 or head_y >= screen_height or head_y < 0:
        return True

    if (head_x, head_y) in snake_list[:-1]:
        return True

    return False

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    head_x, head_y = snake_list[-1]
    if direction == 'UP':
        head_y -= snake_block
    elif direction == 'DOWN':
        head_y += snake_block
    elif direction == 'LEFT':
        head_x -= snake_block
    elif direction == 'RIGHT':
        head_x += snake_block
    snake_head = (head_x, head_y)

    if check_collision(snake_list, snake_block, SCREEN_WIDTH, SCREEN_HEIGHT):
        running = False

    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    if not food_active:
        if pygame.time.get_ticks() - food_timer > 5000:  # Check if 5 seconds have elapsed
            generate_food()

    if snake_head == food_position:
        score += food_weight
        if score % 3 == 0:
            level += 1
            snake_speed += 5
        snake_length += 1
        food_active = False

    for x, y in snake_list:
        pygame.draw.rect(screen, GREEN, [x, y, snake_block, snake_block])

    if food_active:
        pygame.draw.rect(screen, RED, [food_position[0], food_position[1], snake_block, snake_block])

    text = font.render(f"Score: {score}  Level: {level}", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(snake_speed)

pygame.quit()
