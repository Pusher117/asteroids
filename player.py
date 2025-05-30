import pygame
from circleshape import CircleShape
from constants import *
from shots import Shot 

WHITE = (255,255,255)

class Player(CircleShape):
    def __init__(self,x,y): 
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
        self.invincible =False
        self.invincibility_Timer=0

    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, self.triangle(), 2)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self,dt):
        # Update invincibility timer
        if self.invincible:
            self.invincibility_timer -= dt
            if self.invincibility_timer <= 0:
                self.invincible = False
        self.rotation+=PLAYER_TURN_SPEED * dt

    def update(self, dt):
            
            if self.shot_cooldown > 0: 
                 self.shot_cooldown = max(self.shot_cooldown -dt, 0 )
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                self.rotate(-dt)
            if keys[pygame.K_d]:
                self.rotate(dt)
            if keys[pygame.K_w]: 
                 self.move(dt)
            if keys[pygame.K_s]: 
                 self.move(dt)
            if keys[pygame.K_SPACE]: 
                 self.shoot()
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shot_cooldown == 0:
            shot = Shot(self.position.x,self.position.y)
            base_velocity = pygame.Vector2(0,1)
            shot.velocity = base_velocity.rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shot_cooldown = PLAYER_SHOT_COOLDOWN

