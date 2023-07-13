import pygame
import sys
import math

# 게임 화면 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 캐릭터 초기 위치
initial_x = SCREEN_WIDTH // 2
initial_y = SCREEN_HEIGHT // 2

# 색상 정의
BLACK = (0, 0, 0)

def calculate_angle(x, y, mouse_x, mouse_y):
    """캐릭터가 마우스를 향해 보도록 각도를 계산하는 함수"""
    delta_x = mouse_x - x
    delta_y = mouse_y - y
    angle_radians = math.atan2(delta_y, delta_x)
    angle_degrees = math.degrees(angle_radians)
    return angle_degrees

def main():
    pygame.init()

    # 게임 화면 설정
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("캐릭터 움직이기")

    # 캐릭터 이미지 불러오기
    character_image = pygame.image.load("resources/images/slimes.png").convert_alpha()
    character_rect = character_image.get_rect()
    character_rect.center = (initial_x, initial_y)

    # 총 이미지 불러오기
    gun_image = pygame.image.load("resources/images/gun.png").convert_alpha()
    gun_rect = gun_image.get_rect()
    gun_offset = (50, -10)  # 총의 위치 조정

    # 총알 이미지 불러오기
    bullet_image = pygame.image.load("resources/images/bullet.png").convert_alpha()
    bullet_rect = bullet_image.get_rect()
    bullet_speed = 10

    # 배경 이미지 불러오기
    background_image = pygame.image.load("resources/images/wall.png").convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    background_rect = background_image.get_rect()

    clock = pygame.time.Clock()

    bullets = []  # 발사된 총알들을 저장하는 리스트

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 마우스 좌클릭 시 총알 발사
                mouse_x, mouse_y = pygame.mouse.get_pos()
                angle = calculate_angle(character_rect.centerx, character_rect.centery, mouse_x, mouse_y)
                bullet_rect.center = character_rect.center
                bullets.append((bullet_rect.copy(), angle))

        # 키 입력 처리
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            character_rect.move_ip(0, -5)  # 위로 이동
        if keys[pygame.K_s]:
            character_rect.move_ip(0, 5)  # 아래로 이동
        if keys[pygame.K_a]:
            character_rect.move_ip(-5, 0)  # 왼쪽으로 이동
        if keys[pygame.K_d]:
            character_rect.move_ip(5, 0)  # 오른쪽으로 이동

        # 캐릭터가 화면을 벗어나지 않도록 처리
        if character_rect.left < 0:
            character_rect.left = 0
        if character_rect.right > SCREEN_WIDTH:
            character_rect.right = SCREEN_WIDTH
        if character_rect.top < 0:
            character_rect.top = 0
        if character_rect.bottom > SCREEN_HEIGHT:
            character_rect.bottom = SCREEN_HEIGHT

        # 배경 그리기
        screen.blit(background_image, background_rect)

        # 캐릭터 그리기
        character_angle = calculate_angle(character_rect.centerx, character_rect.centery, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        rotated_character = pygame.transform.rotate(character_image, -character_angle)
        character_rect = rotated_character.get_rect(center=character_rect.center)
        screen.blit(rotated_character, character_rect)

        # 총 그리기
        gun_position = (character_rect.centerx + gun_offset[0], character_rect.centery + gun_offset[1])
        screen.blit(gun_image, gun_position)

        # 총알 그리기 및 이동
        new_bullets = []
        for bullet, angle in bullets:
            dx = bullet_speed * math.cos(math.radians(angle))
            dy = bullet_speed * math.sin(math.radians(angle))
            bullet.move_ip(dx, dy)
            if bullet.colliderect(background_rect):
                new_bullets.append((bullet, angle))
            screen.blit(bullet_image, bullet)
        bullets = new_bullets

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
