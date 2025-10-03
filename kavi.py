import pygame
import numpy as np
import math


screen = pygame.display.set_mode((800, 600))
class Ball():
    def __init__(self, position, speed, degree):
        self.WIDTH, self.HEIGHT = 800, 600
        self.ball = pygame.image.load("download.png").convert_alpha()
        self.ball = pygame.transform.scale(self.ball, (100, 100))
        self.ball_rect = self.ball.get_rect(center=position)
        self.vector = pygame.math.Vector2
        self.position = position
        self.velocity = self.vector(0,0)
        self.acceleration = self.vector(0,0)
        self.friction = 0.01
        self.speed = speed
        rad = math.radians(degree)
        self.gravity = self.vector(0, 0.2)
        self.velocity = self.vector(np.cos(rad) * self.speed, np.sin(rad) * self.speed)
        

    
    def ball_movement(self):
        self.acceleration = self.vector(0,0)
        self.acceleration -= self.velocity * self.friction
        self.velocity += self.acceleration
        self.velocity += self.gravity
        
        self.position += self.velocity
        self.ball_rect.center = self.position
        self.ball_collision()




    def ball_collision(self):

        if self.ball_rect.left < 0:
            self.ball_rect.left = 0
            self.position.x = self.ball_rect.centerx
            self.velocity.x *= -1
        if self.ball_rect.right > self.WIDTH:
            self.ball_rect.right = self.WIDTH
            self.position.x = self.ball_rect.centerx
            self.velocity.x *= -1
        if self.ball_rect.top < 0:
            self.ball_rect.top = 0
            self.position.y = self.ball_rect.centery
            self.velocity.y *= -1
        if self.ball_rect.bottom > self.HEIGHT:
            self.ball_rect.bottom = self.HEIGHT
            self.position.y = self.ball_rect.centery
            self.velocity.y *= -1
                
    def draw(self, screen):
        screen.blit(self.ball, self.ball_rect)
    def is_slow(self):
        return self.velocity.length() > 0.1

        
class kavi():
    def __init__(self):
        self.FPS = 60
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.PINK = (255, 182, 193)
        self.DARK_RED = (139, 0, 0)
        self.GREEN = (0, 255, 0)
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 100)
        self.balls = []
        self.WIDTH, self.HEIGHT = 800, 600
        self.rad = 0
        self.new_gen = True
        self.font = pygame.font.Font('LuckiestGuy.ttf',15)
        self.font2 = pygame.font.Font('LuckiestGuy.ttf',50)
        self.soccer = self.font.render("SOCCER BALL", False, self.GREEN)
        self.soccer_rect = self.soccer.get_rect(topleft=((10, 10)))
        background = pygame.image.load("field.png").convert_alpha()
        background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
        self.no_ball = self.font2.render("Click Space", False, self.GREEN)
        self.no_ball_rect = self.no_ball.get_rect(center=((self.WIDTH//2, self.HEIGHT//5)))
        
        while True:

            screen.blit(background, (0, 0))
            screen.blit(self.soccer, self.soccer_rect)
            
            self.game_event()
            
            for ball in self.balls:
                ball.ball_movement()
                ball.draw(screen)
                if not ball.is_slow():
                    self.balls.remove(ball)
                    
            if not self.balls and not self.new_gen:
                screen.blit(self.no_ball, self.no_ball_rect)


            pygame.display.flip()
            pygame.time.Clock().tick(60)
        
    def game_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == self.obstacle_timer:
                if len(self.balls) <= 30 and self.new_gen:
                    self.balls.append(Ball((self.WIDTH//2,self.HEIGHT//2), 30, self.rad))
                    self.rad += 10
                    if len(self.balls) == 30:
                        self.new_gen = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.new_gen = True
                    
                

if __name__ == "__main__":
    pygame.init()
    kavi()
    pygame.quit()
    exit()
    
    