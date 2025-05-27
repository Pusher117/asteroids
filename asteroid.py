import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH

WHITE = (255,255,255)

class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self,screen): 
        pygame.draw.circle(screen,WHITE,self.position,self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt
# Screen wrapping logic
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0

        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
        

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        
        random_angle=random.uniform(20,50)
        
        #2 vectors 
        vect1=self.velocity.rotate(random_angle)
        vect2=self.velocity.rotate(-random_angle)

        new_radius=self.radius - ASTEROID_MIN_RADIUS

        #2new asteroids get made
        a1=Asteroid(self.position.x,self.position.y,new_radius)
        a2=Asteroid(self.position.x,self.position.y,new_radius)

        a1.velocity=vect1*1.2
        a2.velocity=vect2*1.2

        return[a1,a2]