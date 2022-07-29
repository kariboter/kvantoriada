import pygame
import sys
import motors
import smoot_motors

FPS = 60
W = 100
H = 100
WHITE = (255, 255, 255)

motors = motors.Motors()
motors.stop()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# координаты и радиус круга
counter = 0

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motors.rotate_left()
            elif i.key == pygame.K_RIGHT:
                motors.rotate_right()
            elif i.key == pygame.K_UP:
                motors.move_forward()
            elif i.key == pygame.K_DOWN:
                motors.move_backward()
            elif i.key == pygame.K_w:
                if counter < 100:
                    motors.set_servo_max()
                else:
                    break
            elif i.key == pygame.K_s:
                if -100 < counter:
                    motors.set_servo_min()
                else:
                    break
        elif i.type == pygame.KEYUP:
            motors.stop()
    sc.fill(WHITE)
    pygame.display.update()
    clock.tick(FPS)
