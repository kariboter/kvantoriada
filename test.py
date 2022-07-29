import pygame
import sys
from motors import Motors

m = Motors()
FPS = 60
W = 50  # ширина экрана
H = 50  # высота экрана
WHITE = (255, 255, 255)

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# координаты и радиус круга
x = W // 2
y = H // 2
r = 50
m.stop()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    sc.fill(WHITE)
    pygame.display.update()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        m.rotate_left()
    elif keys[pygame.K_RIGHT]:
        m.rotate_right()
    elif keys[pygame.K_UP]:
        m.move_forward()
    elif keys[pygame.K_DOWN]:
        m.move_backward()
    elif keys[pygame.K_w]:
        m.set_servo_value(0.9, -0.9)
    elif keys[pygame.K_s]:
        m.set_servo_value(-0.9, 0.9)
    elif keys[pygame.K_LEFT] == False and keys[pygame.K_RIGHT] == False and keys[pygame.K_UP] == False and keys[pygame.K_DOWN] == False:
        m.stop()

    clock.tick(FPS)
