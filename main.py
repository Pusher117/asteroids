import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shots import *
from gameover import * 

def main(): 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    dt=0
    score= 0
    lives = 3
    font = pygame.font.SysFont(None,36)

#Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable,drawable)
##Spawn player and asteroids
    player=Player(SCREEN_WIDTH /2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
##Game Loop here
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
#update objects        
        for obj in updatable: 
            obj.update(dt)
#collision check
        for asteroid in asteroids: 
            if player.collides(asteroid): 
                lives -=1
                if lives <=0: 
                    game_over_screen(screen,score)
                    return
                player.position=pygame.Vector2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
                player.velocity=pygame.Vector2(0,0)
                break #no double hits

#bullet collusion check
        for asteroid in asteroids: 
            for shot in shots:
                if shot.collides(asteroid): 
                    shot.kill()
                    asteroid.split()
                    base_points = 50
                    MAX_RADIUS = 60
                    score += base_points + int((MAX_RADIUS - asteroid.radius) * 10)
#draw objects after updating            
        for obj in drawable: 
            obj.draw(screen)
#score and life section
        hud_text = f"Score: {score}    Lives: {lives}"
        hud_surface = font.render(hud_text, True, (255, 255, 255))
        screen.blit(hud_surface, (10, 10))  # Top-left corner

        pygame.display.flip()
           
        dt=clock.tick(60) / 1000
if __name__ == "__main__":
    main()