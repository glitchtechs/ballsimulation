import pygame
import sys
import random
import time

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simulation')

black = (0, 0, 0)
white = (255, 255, 255)

class Ball:
    def __init__(self, x, y, speed_x, speed_y, color, radius=20):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color
        self.radius = radius

    def move(self, gravity):
        self.speed_y += gravity
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off walls
        if self.x - self.radius < 0 or self.x + self.radius > width:
            self.speed_x = -self.speed_x
        if self.y - self.radius < 0 or self.y + self.radius > height:
            self.speed_y = -self.speed_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

balls = []

gravity = 0.5

last_spawn_time = time.time()

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time = time.time()
    if current_time - last_spawn_time >= 5:
        new_ball = Ball(
            x=random.randint(20, width - 20),
            y=random.randint(20, height - 20),
            speed_x=random.uniform(-5, 5),
            speed_y=random.uniform(-5, 5),
            color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        )
        balls.append(new_ball)
        last_spawn_time = current_time

    screen.fill(black)
    for ball in balls:
        ball.move(gravity)
        ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)
