import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *

def main(): 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
##Clock object
    clock=pygame.time.Clock()
    dt=0

#Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    Player.containers = (updatable,drawable)
##Spawn player
    player=Player(SCREEN_WIDTH /2, SCREEN_HEIGHT/2)
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
                print ("Game over!")
                sys.exit()
#draw objects after updating            
        for obj in drawable: 
            obj.draw(screen)
        
        pygame.display.flip()
           
        dt=clock.tick(60) / 1000
if __name__ == "__main__":
    main()