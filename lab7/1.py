import pygame
import sys
import time
import math

pygame.init()

width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Clock")
mickey_body = pygame.image.load("mainclock.png")
right_arm = pygame.image.load("rightarm.png")
left_arm = pygame.image.load("leftarm.png")

arm_scale = 0.28
right_arm = pygame.transform.scale(right_arm, (int(right_arm.get_width() * arm_scale), int(right_arm.get_height() * arm_scale)))
left_arm = pygame.transform.scale(left_arm, (int(left_arm.get_width() * arm_scale), int(left_arm.get_height() * arm_scale)))

mickey_rect = mickey_body.get_rect(center=(width // 2, height // 2))

def update_clock():
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    seconds_angle = (seconds / 60) * 360
    minutes_angle = (minutes / 60) * 360

    rotated_right_arm = pygame.transform.rotate(right_arm, -seconds_angle)
    rotated_left_arm = pygame.transform.rotate(left_arm, -minutes_angle)

    right_arm_pos = (mickey_rect.centerx - rotated_right_arm.get_width() // 2,
                     mickey_rect.centery - rotated_right_arm.get_height() // 2)
    left_arm_pos = (mickey_rect.centerx - rotated_left_arm.get_width() // 2,
                    mickey_rect.centery - rotated_left_arm.get_height() // 2)

    screen.fill((255, 255, 255))
    screen.blit(mickey_body, mickey_rect)
    screen.blit(rotated_right_arm, right_arm_pos)
    screen.blit(rotated_left_arm, left_arm_pos)

    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    update_clock()
    pygame.time.wait(1000)   