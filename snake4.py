import pygame
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
CELL = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Multi Apple Version")
clock = pygame.time.Clock()

# Colors
PURPLE = (160, 32, 240)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Snake
snake_pos = [[WIDTH // 2, HEIGHT // 2]]
snake_dir = "RIGHT"
snake_speed = 10

# Apple settings
APPLE_COUNT = 3
apples = []

def spawn_apple():
    return [random.randrange(0, WIDTH, CELL), random.randrange(0, HEIGHT, CELL)]

for _ in range(APPLE_COUNT):
    apples.append(spawn_apple())

score = 0
font = pygame.font.SysFont(None, 35)

def draw_snake():
    for i, pos in enumerate(snake_pos):
        pygame.draw.rect(screen, PURPLE, (pos[0], pos[1], CELL, CELL))

    # Draw face on head
    head_x, head_y = snake_pos[0]
    eye_size = 4
    pygame.draw.circle(screen, WHITE, (head_x + 6, head_y + 6), eye_size)
    pygame.draw.circle(screen, WHITE, (head_x + 14, head_y + 6), eye_size)
    pygame.draw.circle(screen, BLACK, (head_x + 6, head_y + 6), 2)
    pygame.draw.circle(screen, BLACK, (head_x + 14, head_y + 6), 2)
    pygame.draw.rect(screen, BLACK, (head_x + 6, head_y + 14, 8, 3))


def move_snake():
    head = snake_pos[0].copy()

    if snake_dir == "UP":
        head[1] -= CELL
    elif snake_dir == "DOWN":
        head[1] += CELL
    elif snake_dir == "LEFT":
        head[0] -= CELL
    elif snake_dir == "RIGHT":
        head[0] += CELL

    snake_pos.insert(0, head)


def check_collisions():
    global score

    # Wall collision
    if (
        snake_pos[0][0] < 0
        or snake_pos[0][0] >= WIDTH
        or snake_pos[0][1] < 0
        or snake_pos[0][1] >= HEIGHT
    ):
        return True

    # Self collision
    if snake_pos[0] in snake_pos[1:]:
        return True

    # Apple collision
    for apple in apples:
        if snake_pos[0] == apple:
            score += 1
            apples.remove(apple)
            apples.append(spawn_apple())
            return False

    # If no apple eaten, remove tail
    snake_pos.pop()
    return False


def draw_apples():
    for apple in apples:
        pygame.draw.rect(screen, RED, (apple[0], apple[1], CELL, CELL))


def main():
    global snake_dir
    running = True

    while running:
        clock.tick(snake_speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_dir != "DOWN":
                    snake_dir = "UP"
                if event.key == pygame.K_DOWN and snake_dir != "UP":
                    snake_dir = "DOWN"
                if event.key == pygame.K_LEFT and snake_dir != "RIGHT":
                    snake_dir = "LEFT"
                if event.key == pygame.K_RIGHT and snake_dir != "LEFT":
                    snake_dir = "RIGHT"

        move_snake()

        if check_collisions():
            running = False

        screen.fill(BLACK)
        draw_snake()
        draw_apples()

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
