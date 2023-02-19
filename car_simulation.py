import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((900, 900))

car_image = pygame.image.load("car.png")

car_image_rect = car_image.get_rect()

car_x = 300
car_y = 300

# Define movement speed
speed = 0.2

acceleration = 0.002

angle = 0

rotation_speed = 0.1

# Main game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        speed += acceleration
        car_y -= speed
    if keys[pygame.K_DOWN]:
        speed = 0.12
        car_y += speed
    if keys[pygame.K_LEFT]:
        angle += rotation_speed
    if keys[pygame.K_RIGHT]:
        angle -= rotation_speed

    #Rotate car 
    rotated_image = pygame.transform.rotate(car_image, angle)
    rotated_image_rect = rotated_image.get_rect()
    screen.fill((255, 255, 255))
    screen.blit(rotated_image, (car_x, car_y), rotated_image_rect)

    pygame.display.update()
