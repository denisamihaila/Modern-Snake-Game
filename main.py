import pygame
import sys
import random
import os

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Advanced Snake Game')

BLACK = (0, 0, 0)

CLOCK = pygame.time.Clock()
SNAKE_SPEED = 7.5  # Initial speed (FPS)

BLOCK_SIZE = 40

FONT_SCORE = pygame.font.SysFont("bahnschrift", 35)
FONT_MESSAGE = pygame.font.SysFont("comicsansms", 50, bold=True)

HIGH_SCORE_FILE = "highscore.txt"

try:
    BACKGROUND_IMAGE = pygame.image.load('images/background.jpg')
    BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))

    SNAKE_HEAD_IMAGE = pygame.image.load('images/snakehead.png')
    SNAKE_HEAD_IMAGE = pygame.transform.scale(SNAKE_HEAD_IMAGE, (BLOCK_SIZE, BLOCK_SIZE))

    SNAKE_BODY_IMAGE = pygame.image.load('images/snakebody.png')
    SNAKE_BODY_IMAGE = pygame.transform.scale(SNAKE_BODY_IMAGE, (BLOCK_SIZE, BLOCK_SIZE))

    FOOD_IMAGE = pygame.image.load('images/food.png')
    FOOD_IMAGE = pygame.transform.scale(FOOD_IMAGE, (BLOCK_SIZE, BLOCK_SIZE))

    ENEMY_IMAGE = pygame.image.load('images/enemy.jpg')
    ENEMY_IMAGE = pygame.transform.scale(ENEMY_IMAGE, (BLOCK_SIZE, BLOCK_SIZE))
except pygame.error as e:
    print(f"Error loading images: {e}")
    print("Ensure that the images 'background.jpg', 'snakehead.png', 'snakebody.png', 'food.png', and 'enemy.jpg' are in the 'images/' directory.")
    pygame.quit()
    sys.exit()

def read_high_score():
    if not os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, 'w') as f:
            f.write("0")
    with open(HIGH_SCORE_FILE, 'r') as f:
        try:
            return int(f.read())
        except:
            return 0

def save_high_score(score):
    high_score = read_high_score()
    if score > high_score:
        with open(HIGH_SCORE_FILE, 'w') as f:
            f.write(str(score))

class Snake:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.change_x = 0
        self.change_y = 0
        self.body = []
        self.length = 1

    def move(self):
        self.x += self.change_x
        self.y += self.change_y
        head = [self.x, self.y]
        self.body.append(head)
        if len(self.body) > self.length:
            del self.body[0]

    def draw(self, screen):
        if len(self.body) > 0:
            # Draw the head
            SCREEN.blit(SNAKE_HEAD_IMAGE, (self.body[-1][0], self.body[-1][1]))
            # Draw the body
            for segment in self.body[:-1]:
                SCREEN.blit(SNAKE_BODY_IMAGE, (segment[0], segment[1]))

    def get_head_rect(self):
        return pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

class Food:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.reset()

    def reset(self):
        self.x = random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
        self.y = random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

    def draw(self, screen):
        SCREEN.blit(FOOD_IMAGE, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

class Enemy:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.reset()

    def reset(self):
        self.x = random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
        self.y = random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

    def draw(self, screen):
        SCREEN.blit(ENEMY_IMAGE, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

def display_score(score):
    text = FONT_SCORE.render(f"Score: {score}", True, BLACK)
    SCREEN.blit(text, [10, 10])

def display_high_score(high_score):
    text = FONT_SCORE.render(f"High Score: {high_score}", True, BLACK)
    SCREEN.blit(text, [SCREEN_WIDTH - 250, 10])

def display_message(msg, color):
    text = FONT_MESSAGE.render(msg, True, color)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    SCREEN.blit(text, text_rect)

def game_snake():
    global SNAKE_SPEED

    game_over = False
    closed_game = False

    snake = Snake()
    food = Food()
    enemies = []

    # Adding initial enemies
    for _ in range(3):
        enemy = Enemy()
        # Ensure not placed over food or snake
        while [enemy.x, enemy.y] in snake.body or [enemy.x, enemy.y] == [food.x, food.y]:
            enemy.reset()
        enemies.append(enemy)

    level = 1
    points_per_level = 3
    current_score = 0
    high_score = read_high_score()

    while not game_over:

        while closed_game:
            SCREEN.blit(BACKGROUND_IMAGE, (0, 0))
            display_message("Q - Exit   C - Try Again", BLACK)
            display_score(current_score)
            display_high_score(high_score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        save_high_score(current_score)
                        game_over = True
                        closed_game = False
                    if event.key == pygame.K_c:
                        save_high_score(current_score)
                        game_snake()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_high_score(current_score)
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.change_x != BLOCK_SIZE:
                    snake.change_x = -BLOCK_SIZE
                    snake.change_y = 0
                elif event.key == pygame.K_RIGHT and snake.change_x != -BLOCK_SIZE:
                    snake.change_x = BLOCK_SIZE
                    snake.change_y = 0
                elif event.key == pygame.K_UP and snake.change_y != BLOCK_SIZE:
                    snake.change_y = -BLOCK_SIZE
                    snake.change_x = 0
                elif event.key == pygame.K_DOWN and snake.change_y != -BLOCK_SIZE:
                    snake.change_y = BLOCK_SIZE
                    snake.change_x = 0

        if snake.x >= SCREEN_WIDTH + 1 or snake.x < -1 or snake.y >= SCREEN_HEIGHT + 1 or snake.y < -1:
            closed_game = True

        snake.move()

        SCREEN.blit(BACKGROUND_IMAGE, (0, 0)) 

        food.draw(SCREEN)

        for enemy in enemies:
            enemy.draw(SCREEN)

        snake.draw(SCREEN)

        display_score(current_score)
        display_high_score(high_score)

        pygame.display.update()

        # Collision with food
        snake_head_rect = snake.get_head_rect()
        food_rect = food.get_rect()
        if snake_head_rect.colliderect(food_rect):
            snake.length += 1
            current_score += 1
            food.reset()

            # Add an enemy each level
            if current_score % points_per_level == 0:
                level += 1
                SNAKE_SPEED += 2
                enemy = Enemy()
                # Ensure not placed over food or snake
                while [enemy.x, enemy.y] in snake.body or [enemy.x, enemy.y] == [food.x, food.y]:
                    enemy.reset()
                enemies.append(enemy)

        # Collision with own body
        for segment in snake.body[:-1]:
            if segment == [snake.x, snake.y]:
                closed_game = True

        # Collision with enemies
        for enemy in enemies:
            enemy_rect = enemy.get_rect()
            if snake_head_rect.colliderect(enemy_rect):
                closed_game = True

        CLOCK.tick(SNAKE_SPEED)

    pygame.quit()
    sys.exit()

game_snake()
