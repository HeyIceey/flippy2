# ------------------------------------------------------------------------------------------------------------------------
# Himanish 
# ------------------------------------------------------------------------------------------------------------------------
# 22 May 2023 - 22 June 2023
# Final Version
# All Assets Found From Different Sites/Resourses
# -----------------------------------------------------------------------------------------------------------------
# FLIPPY!
# -----------------------------------------------------------------------------------------------------------------

# NOTES
# The game's function is now reversed, The game only fails when you attempt to pass through the pipe gaps.
# You're able to pass through/behind the pipes, only the gaps are collision sensitive.
# Pressing X (Close) will only work when the game's running, and not when the game ends.
# Have fun! 

# ------------------------------------------------------------------------------------------------------------------
# START

import pygame
import sys, random
print("\033c")
# Pygame Initialize
pygame.init()

# FPS
FPS = 60

# Score Stack
score = 0

# SCREEN DIMENSIONS
WIDTH, HEIGHT = 1280, 720

# BACKGROUND IMAGE + REIZE
BG = pygame.transform.scale(pygame.image.load("BG.png"), (WIDTH, HEIGHT))
W = pygame.display.set_mode((WIDTH, HEIGHT))

# TITLE [NAME]
pygame.display.set_caption("FLIPPY: REVERSED!")
# TOP ICON [BIRDIE]
ICON = pygame.image.load("Icon.png")
pygame.display.set_icon(ICON)

# COLORS [MAY/MAY NOT BE USED ATER]
WHITE_BG = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# MENU'S BACKGROUND IMAGE
MenuBG = pygame.transform.scale(pygame.image.load("Menu.png"), (WIDTH, HEIGHT))
# ----------------------------------------------------------------------------------------------------------------

# Load Pipe Images [Scaled/Transformed Later]
PipeDown1 = pygame.image.load("Pipe Up.png")
PipeUp1 = pygame.image.load("Pipe Down.png")

# Background position
bg_x = 0
# Bird Image & Dimensions
bird_height = 86
bird_width = 89 
bird_img = pygame.transform.scale(pygame.image.load("! Birdie.png"), (bird_width, bird_height))
second_bird_img = pygame.transform.scale(pygame.image.load("!2 Birdie.png"), (bird_width, bird_height))

# Bird Dimensions
bird_x = WIDTH // 2 - bird_img.get_width() // 2
bird_y = HEIGHT // 2 - bird_img.get_height() // 2
second_bird_x = bird_x + 100  # Adjust the position of the second bird
second_bird_y = bird_y

bird_speed = 5.39 # Moving Speed [Optimized] [Vertical]
jump_speed = -12.8  # Jump Speed [Somewhat Optimized]

is_jump = False
second_is_jump = False

jump_count = 22
second_jump_count = 22

# Pipe Dimensions
pipe_width = 250
pipe_gap = 120
pipe_x = WIDTH
pipe_speed = 9.6  # How fast pipe pass through
pipe_height = random.randint(200, HEIGHT - pipe_gap - 200)
pipe_y = pipe_height + pipe_gap

# Pipe Images
PipeUp = pygame.transform.scale(pygame.image.load("Pipe Down.png"), (pipe_width, HEIGHT))
PipeDown = pygame.transform.scale(pygame.image.load("Pipe Up.png"), (pipe_width, HEIGHT))

# Collision Logic [CHANGED] [Help from GitHub, Google, YT, GPT]
def check_collision():
    if (bird_y + bird_height > pipe_height and bird_y < pipe_y) or \
            (second_bird_y + bird_height > pipe_height and second_bird_y < pipe_y):
        if bird_x + bird_width > pipe_x and bird_x < pipe_x + pipe_width:
            return True
        if second_bird_x + bird_width > pipe_x and second_bird_x < pipe_x + pipe_width:
            return True
    return False

# [Initial Menu]
def menu():
    while True:
        W.blit(MenuBG, (0, 0))  # BG + SIZE

        # Display menu text [Added more text and basic instructions]
        font = pygame.font.SysFont('Century Gothic', 55)  # FONT & SIZE
        text1 = font.render("Press Spacebar to start, Work as a team!", True, WHITE_BG)
        text2 = font.render("Blue = Spacebar, Yellow = Enter!", True, WHITE_BG)
        text3 = font.render("Gaps are Dangerous, Pass thru the pipes!", True, WHITE_BG)
        text1_rect = text1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
        text2_rect = text2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
        text3_rect = text3.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 90))

        W.blit(text1, text1_rect)
        W.blit(text2, text2_rect)
        W.blit(text3, text3_rect)


        pygame.display.update()  # UPDATE DISPLAY

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return


# Update Pipes, Randomizes Size
def update_pipes():
    global pipe_x, pipe_height, pipe_y, score

    pipe_x -= pipe_speed

    if pipe_x < -pipe_width:
        pipe_x = WIDTH
        pipe_height = random.randint(200, HEIGHT - pipe_gap - 200)
        pipe_y = pipe_height + pipe_gap

        # Change score when going thru the pipe
        score += 1

def draw_window():
    global bg_x, bird_y, second_bird_y, is_jump, second_is_jump, jump_count, second_jump_count, pipe_x, pipe_height, pipe_y, score

    # Scroll the background image horizontally
    bg_x -= bird_speed
    if bg_x < -WIDTH:
        bg_x = 0

    W.fill(WHITE_BG)
    W.blit(BG, (bg_x, 0))
    W.blit(BG, (bg_x + WIDTH, 0))  # Draw a second copy to create a seamless loop

    # Handle bird jumping
    if is_jump:
        if jump_count >= -8:
            bird_y += jump_speed
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 8

    if second_is_jump:
        if second_jump_count >= -8:
            second_bird_y += jump_speed
            second_jump_count -= 1
        else:
            second_is_jump = False
            second_jump_count = 8

    # Update bird positions
    bird_y += bird_speed
    second_bird_y += bird_speed

    # Draw the bird images
    W.blit(bird_img, (bird_x, bird_y))
    W.blit(second_bird_img, (second_bird_x, second_bird_y))

    # Update and draw the pipes
    update_pipes()
    W.blit(PipeUp, (pipe_x, pipe_height - HEIGHT))
    W.blit(PipeDown, (pipe_x, pipe_y))

    # SCORE [NEW ADDON]
    font = pygame.font.SysFont('Century Gothic', 30)
    score_text = font.render(f"Score: {score}", True, WHITE_BG)
    score_text_rect = score_text.get_rect(topright=(WIDTH - 20, 20))
    W.blit(score_text, score_text_rect)
    
    
    # [NEW ADDON]
    
    # Collision check
    if check_collision():
        # Game over message
        font = pygame.font.SysFont('Century Gothic', 80)
        game_over_text = font.render("Game Over", True, BLACK)
        game_over_text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

        # Retry message
        font = pygame.font.SysFont('Century Gothic', 40)
        retry_text = font.render("Press Spacebar to Retry", True, BLACK)
        retry_text_rect = retry_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

        # Draw game over and retry messages on the screen
        W.blit(game_over_text, game_over_text_rect)
        W.blit(retry_text, retry_text_rect)

        pygame.display.update()

        # Wait for spacebar to be pressed to retry
        spacebar_pressed = False
        while not spacebar_pressed:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        spacebar_pressed = True

        # Reset game state
        score = 0
        bird_y = HEIGHT // 2 - bird_img.get_height() // 2
        second_bird_y = bird_y
        pipe_x = WIDTH
        pipe_height = random.randint(200, HEIGHT - pipe_gap - 200)
        pipe_y = pipe_height + pipe_gap

        # Reset jump state
        is_jump = False
        second_is_jump = False
        jump_count = 22
        second_jump_count = 22

    pygame.display.update()

clock = pygame.time.Clock()
menu()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jump:
                is_jump = True
                jump_count = 10
            if event.key == pygame.K_RETURN and not second_is_jump:
                second_is_jump = True
                second_jump_count = 10

    draw_window()
    clock.tick(FPS)

# End
pygame.quit()
print("Thanks for playing!\n")
print("Have a great day!\n")
quit()

# Bye! :D
# Original Finished 6 June 2023
# Final Finished 23 June 2023 :) 
# Have a great summer!

# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------