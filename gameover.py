import pygame
import sys

def game_over_screen(screen, score):
    font = pygame.font.SysFont(None, 48)
    small_font = pygame.font.SysFont(None, 32)

    screen.fill((0, 0, 0))
    game_over_text = font.render("GAME OVER", True, (255, 0, 0))
    score_text = small_font.render(f"Final Score: {score}", True, (255, 255, 255))
    restart_text = small_font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))

    screen_rect = screen.get_rect()
    screen.blit(game_over_text, game_over_text.get_rect(center=(screen_rect.centerx, screen_rect.centery - 50)))
    screen.blit(score_text, score_text.get_rect(center=(screen_rect.centerx, screen_rect.centery)))
    screen.blit(restart_text, restart_text.get_rect(center=(screen_rect.centerx, screen_rect.centery + 50)))

    pygame.display.flip()

    # Wait for player input to restart or quit
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False  # Exit and restart the game
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
