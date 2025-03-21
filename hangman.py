import pygame
import random
import base64

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE, BLACK, RED = (255, 255, 255), (0, 0, 0), (200, 0, 0)
FONT_NAME = "Arial"

hangman_images = [pygame.image.load(f"./hangman/{i}.png") for i in range(8)]  
win_image = pygame.image.load("./hangman/w.png")

# Read and decode words from file
with open("words.txt", "r") as file:
    encoded_words = file.read().strip()
    words = base64.b64decode(encoded_words).decode().split(",")

word = random.choice(words).lower()
guessed_word = ["_"] * len(word)
guessed_letters = set()
attempts = 7

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Swiftie Hangman 🎶")

font = pygame.font.SysFont(FONT_NAME, 40)
small_font = pygame.font.SysFont(FONT_NAME, 30)

def draw_game():
    screen.fill(WHITE)
    screen.blit(hangman_images[7 - attempts], (100, 100))
    word_display = font.render(" ".join(guessed_word), True, BLACK)
    screen.blit(word_display, (300, 450))
    guessed_text = small_font.render(f"Guessed: {', '.join(sorted(guessed_letters))}", True, BLACK)
    screen.blit(guessed_text, (300, 500))
    attempts_text = small_font.render(f"Attempts Left: {attempts}", True, RED)
    screen.blit(attempts_text, (600, 50))
    pygame.display.update()

def display_win():
    screen.fill(WHITE)
    screen.blit(win_image, (WIDTH//2 - 100, HEIGHT//2 - 100))
    text = font.render("🎉 You Won, Swiftie! 🎶", True, BLACK)
    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT - 100))
    pygame.display.update()
    pygame.time.delay(2000)

def display_loss():
    screen.fill(WHITE)
    screen.blit(hangman_images[7], (100, 100))
    text = font.render(f"💔 Game Over! The word was '{word}'", True, RED)
    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT - 100))
    pygame.display.update()
    pygame.time.delay(2000)

running = True
while running:
    draw_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            guess = event.unicode.lower()
            if guess.isalpha() and guess not in guessed_letters:
                guessed_letters.add(guess)
                if guess in word:
                    for i, letter in enumerate(word):
                        if letter == guess:
                            guessed_word[i] = guess
                else:
                    attempts -= 1

    if "_" not in guessed_word:
        display_win()
        break

    if attempts == 0:
        display_loss()
        break

pygame.quit()
