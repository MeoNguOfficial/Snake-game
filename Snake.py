import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Đặt kích thước cố định cho cửa sổ
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900

# Đặt chế độ cửa sổ với kích thước 1600x900
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Rắn săn mồi")

# Các màu
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE = (153, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Kích thước rắn, thức ăn và chướng ngại vật
SNAKE_SIZE = 20
FOOD_SIZE = 20
OBSTACLE_SIZE = SNAKE_SIZE

# Tốc độ rắn
SNAKE_SPEED = SNAKE_SIZE
game_speed = 10  # Mặc định tốc độ game
level = 1  # Cấp độ ban đầu

# Hệ số điểm tương ứng với mỗi cấp độ
score_multiplier = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

# Khởi tạo font chữ để hiển thị điểm số
font = pygame.font.SysFont(None, 35)

# Khởi tạo high scores cho từng level
high_scores = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
invert_high_scores = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}  # High score cho Invert Control

# Tải âm thanh
eat_food_sound = pygame.mixer.Sound("../Game1/Resources/eat_food.mp3")
pause_game_sound = pygame.mixer.Sound("../Game1/Resources/pause_game.mp3")
high_score_sound = pygame.mixer.Sound("../Game1/Resources/high_score.mp3")
invert_control_sound = pygame.mixer.Sound("../Game1/Resources/invert_control.mp3")
game_over_sound = pygame.mixer.Sound("../Game1/Resources/game_over.mp3")

# Tải nhạc nền
pygame.mixer.music.load("../Game1/Resources/start_game.mp3")
pygame.mixer.music.set_volume(0.5)  # Điều chỉnh âm lượng nếu cần

def new_game():
    global snake, score, food, obstacles, direction, game_started, game_paused, running, start_time, game_over_time
    global invert_control
    snake = [(WINDOW_WIDTH // 2 // SNAKE_SIZE * SNAKE_SIZE,
               WINDOW_HEIGHT // 2 // SNAKE_SIZE * SNAKE_SIZE)]
    score = 0
    food = (random.randint(0, (WINDOW_WIDTH - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE,
            random.randint(0, (WINDOW_HEIGHT - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE)
    obstacles = []
    direction = "right"
    game_started = False
    game_paused = False
    running = True
    start_time = None
    game_over_time = None
    invert_control = False
    pygame.mixer.music.play(-1)  # Phát nhạc nền liên tục

def update_music_speed(level):
    # Điều chỉnh tốc độ nhạc căn cứ vào level
    speed_factor = 1 + (0.2 * (level - 1))  # mỗi level tăng 20%
    pygame.mixer.music.set_volume(0.5 * speed_factor)  # Tăng tốc độ âm thanh

def game_over():
    global running, game_started, game_over_time, high_scores, invert_high_scores
    game_over_time = pygame.time.get_ticks()
    game_over_sound.play()  # Phát âm thanh khi game over

    # Dừng nhạc nền khi game over
    pygame.mixer.music.stop()

    if invert_control:
        if score > invert_high_scores[level]:
            invert_high_scores[level] = score
            high_score_sound.play()  # Phát âm thanh ghi điểm cao cho Invert Control
    else:
        if score > high_scores[level]:
            high_scores[level] = score
            high_score_sound.play()  # Phát âm thanh ghi điểm cao
    game_started = False

def start_game():
    global running, start_time
    start_time = pygame.time.get_ticks()

new_game()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_paused = not game_paused
                if game_paused:
                    pause_game_sound.play()  # Phát âm thanh khi tạm dừng trò chơi
                    pygame.mixer.music.pause()  # Tạm dừng nhạc nền

            elif event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                if not game_started: 
                    game_started = True
                
                if invert_control:
                    if event.key == pygame.K_LEFT and direction != "right":
                        direction = "right"
                    elif event.key == pygame.K_RIGHT and direction != "left":
                        direction = "left"
                    elif event.key == pygame.K_UP and direction != "down":
                        direction = "down"
                    elif event.key == pygame.K_DOWN and direction != "up":
                        direction = "up"
                else:
                    if event.key == pygame.K_LEFT and direction != "right":
                        direction = "left"
                    elif event.key == pygame.K_RIGHT and direction != "left":
                        direction = "right"
                    elif event.key == pygame.K_UP and direction != "down":
                        direction = "up"
                    elif event.key == pygame.K_DOWN and direction != "up":
                        direction = "down"

                if game_over_time:
                    new_game()
                    start_game()

            elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5]:
                new_game()
                score = 0
                if event.key == pygame.K_1:
                    game_speed = 10
                    level = 1
                elif event.key == pygame.K_2:
                    game_speed = 20
                    level = 2
                elif event.key == pygame.K_3:
                    game_speed = 30
                    level = 3
                elif event.key == pygame.K_4:
                    game_speed = 40
                    level = 4
                elif event.key == pygame.K_5:
                    game_speed = 50
                    level = 5
                
                update_music_speed(level)  # Cập nhật tốc độ nhạc theo cấp độ

            elif event.key == pygame.K_SPACE:
                invert_control = not invert_control  # Đảo chiều điều khiển
                invert_control_sound.play()  # Phát âm thanh khi đảo chiều điều khiển

    if game_started and not game_paused:
        new_head = list(snake[-1])
        if direction == "right":
            new_head[0] += SNAKE_SPEED
        elif direction == "left":
            new_head[0] -= SNAKE_SPEED
        elif direction == "up":
            new_head[1] -= SNAKE_SPEED
        elif direction == "down":
            new_head[1] += SNAKE_SPEED

        if (new_head[0] < 0 or new_head[0] >= WINDOW_WIDTH or
            new_head[1] < 0 or new_head[1] >= WINDOW_HEIGHT):
            game_over()

        if tuple(new_head) in snake:
            game_over()

        for obstacle in obstacles:
            if (new_head[0] >= obstacle[0] and new_head[0] < obstacle[0] + OBSTACLE_SIZE and
                new_head[1] >= obstacle[1] and new_head[1] < obstacle[1] + OBSTACLE_SIZE):
                game_over()

        if (new_head[0] >= food[0] and new_head[0] < food[0] + FOOD_SIZE and
            new_head[1] >= food[1] and new_head[1] < food[1] + FOOD_SIZE):
            food = (random.randint(0, (WINDOW_WIDTH - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE,
                    random.randint(0, (WINDOW_HEIGHT - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE)
            score += score_multiplier[level]
            eat_food_sound.play()  # Phát âm thanh khi ăn thức ăn

            if score % 1 == 0:
                while True:
                    new_obstacle = (random.randint(0, (WINDOW_WIDTH - OBSTACLE_SIZE) // OBSTACLE_SIZE) * OBSTACLE_SIZE,
                                    random.randint(0, (WINDOW_HEIGHT - OBSTACLE_SIZE) // OBSTACLE_SIZE) * OBSTACLE_SIZE)
                    if new_obstacle not in snake and new_obstacle != food and new_obstacle not in obstacles:
                        obstacles.append(new_obstacle)
                        break
        else:
            snake.pop(0)

        snake.append(tuple(new_head))

    window.fill(BLACK)
    for x in range(0, WINDOW_WIDTH, SNAKE_SIZE):
        pygame.draw.line(window, (50, 50, 50), (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, SNAKE_SIZE):
        pygame.draw.line(window, (50, 50, 50), (0, y), (WINDOW_WIDTH, y))

    for segment in snake:
        pygame.draw.rect(window, GREEN, pygame.Rect(segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))
    pygame.draw.rect(window, WHITE, pygame.Rect(food[0], food[1], FOOD_SIZE, FOOD_SIZE))
    for obstacle in obstacles:
        pygame.draw.rect(window, RED, pygame.Rect(obstacle[0], obstacle[1], OBSTACLE_SIZE, OBSTACLE_SIZE))

    score_surface = font.render(f'Score: {score}', True, WHITE)
    window.blit(score_surface, (10, 10))

    if invert_control:
        high_score_surface = font.render(f'Invert High Score: {invert_high_scores[level]}', True, YELLOW)
    else:
        high_score_surface = font.render(f'High Score: {high_scores[level]}', True, YELLOW)
    window.blit(high_score_surface, (10, 40))

    level_text = f'Level {level}'
    level_surface = font.render(level_text, True, WHITE)
    window.blit(level_surface, (WINDOW_WIDTH - 100, 10))

    multiplier_surface = font.render(f'Boost: x{score_multiplier[level]}', True, YELLOW)
    window.blit(multiplier_surface, (WINDOW_WIDTH - 125, 40))

    if not game_started:
        if start_time and pygame.time.get_ticks() - start_time < 5000:
            start_game_surface = font.render("Press any arrow key to start!", True, WHITE)
            start_game_rect = start_game_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            window.blit(start_game_surface, start_game_rect)
    elif not game_paused:
        if game_over_time:
            if pygame.time.get_ticks() - game_over_time < 5000:
                game_over_surface = font.render("Game Over! Press any arrow key to restart.", True, RED)
                game_over_rect = game_over_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
                window.blit(game_over_surface, game_over_rect)
        else:
            if game_paused:
                pause_surface = font.render("Game paused...", True, WHITE)
                pause_rect = pause_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
                window.blit(pause_surface, pause_rect)

    pygame.display.flip()
    pygame.time.Clock().tick(game_speed)

pygame.quit()
