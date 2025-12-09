import pygame
import sys

# Resolution (16:9 ratio)
WIDTH = 1280
HEIGHT = 720

def start_game_window():
    pygame.init()
    pygame.display.set_caption("PokePi")

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        # ---- Events ----
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # ---- Drawing ----
        screen.fill((20, 20, 20))  # dark background for now

        # Example: draw a placeholder tile rectangle
        pygame.draw.rect(screen, (80, 180, 80), (100, 100, 300, 200))

        pygame.display.flip()
        clock.tick(60)  # 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    start_game_window()
