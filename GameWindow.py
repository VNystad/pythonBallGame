import pygame
import random
import time
import math

width = 600;
height = 500;
# Color (RED, GREEN, BLUE)
background_color = (255,255,205)
balls = 1
ballList = []


drag = 0.999
elasticity = 0.75
# Gravity vector somehow?
gravityAngle = math.pi
gravityLength = 0.002

timeElapsed = 0
tickStart = 0
tickEnd = 0

def addVectors(angle1, length1, angle2, length2):
    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1) * length1 + math.cos(angle2) * length2

    angle = 0.5 * math.pi - math.atan2(y, x)
    length = math.hypot(x, y)

    return (angle, length)

class Ball:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (0, 0, 255)
        self.thickness = 10
        self.angle = math.pi/2
        self.speed = 0.01

    def display(self, window):
        pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), self.size, self.thickness)

    def move(self):
        (self.angle, self.speed) = addVectors(self.angle, self.speed, gravityAngle, gravityLength)
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.speed *= drag

    def bounce(self):
        if self.x > width - self.size:
            self.x = 2*(width - self.size) - self.x
            self.angle = -self.angle
            self.speed *= elasticity

        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = -self.angle
            self.speed *= elasticity

        if self.y > height - self.size:
            self.y = 2 * (height - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

        elif self.y < self.size:
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

def game():
    # Must be a double parenthesis
    window = pygame.display.set_mode((width, height))

    for count in range(balls):
        size = random.randint(10, 20)
        x = random.randint(0, width)
        y = random.randint(0, height)

        ball = Ball(x, y, size)
        ball.speed = random.random()
        ball.angle = random.uniform(0, math.pi/2)

        ballList.append(ball)

    # Title
    pygame.display.set_caption('myGame')

    running = True

    while running:
        tick(window, running)

def tick(window, running):
    global timeElapsed
    global tickStart
    global tickEnd
    timeElapsed = tickEnd - tickStart
    if timeElapsed > 1/60:
        tickStart = time.time()
        timeElapsed = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(background_color)
        for ball in ballList:
            ball.move()
            ball.bounce()
            ball.display(window)

        pygame.display.flip()

    tickEnd = time.time()


if __name__ == '__main__':
    game()