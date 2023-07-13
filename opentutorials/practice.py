import pygame   # 1. 파이게임 모듈을 불러온다
import math
pygame.init()   # 2. 초기화 시킨다

width, height = 640, 480    # 변수 여러개 동시에 정의 가능
screen = pygame.display.set_mode((width, height))
acc = [0,0] # 총알 몇개인지, 죽인 적 수
bullets = []


# 3. 이미지를 가져온다
slime = pygame.image.load("opentutorials/resources/images/slimes.png") # 슬라임 이미지 불러오기
slime = pygame.transform.scale(slime, (80,80)) # 크기 64x64로 변경
slime = pygame.transform.flip(slime, True, False) # 좌우 반전 시키기
bottom = pygame.image.load("opentutorials/resources/images/wall1.png")
tower = pygame.image.load("opentutorials/resources/images/slime_top.png")
bullet = pygame.image.load("opentutorials/resources/images/bullet.png")
gun = pygame.image.load("opentutorials/resources/images/gun.png")
gun = pygame.transform.scale(gun, (60,60))
gun = pygame.transform.rotate(gun, 180)


# 키보드로 움직이기
keys = [False, False, False, False] # w a s d
playpos = [100, 100]



# 4. 계속 화면이 보이도록 한다.

while True:
    # 5. 화면을 깨끗하게 한다.
    screen.fill((0,0,0))

    # 6. 모든 요소들을 다시 그린다.
    for x in range(width//bottom.get_width()+1): # 스크린폭을 이미지의 폭으로 나눈후 정수로 변환(// 이용)
        for y in range(height//bottom.get_height()+1):
            screen.blit(bottom, (x*100,y*100))

    screen.blit(tower, (0, 30))
    screen.blit(tower, (0, 135))
    screen.blit(tower, (0, 240))
    screen.blit(tower, (0, 345))
    
    # 6-2 총알 그리기
    for bul in bullets:
        index = 0
        velx=math.cos(bul[0])*10
        vely=math.sin(bul[0])*10
        bul[1]+=velx
        bul[2]+=vely
        if bul[1] < -64 or bul[1] > 640 or bul[2] < -64 or bul[2] > 480:
            bullets.pop(index)
        index += 1
        for projectile in bullets:
            bullet1 = pygame.transform.rotate(bullet, 360-projectile[0]*57.29)
            screen.blit(bullet1, (projectile[1], projectile[2]))


    # 6-1. 플레이어 위치와 회전 바꾸기
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playpos[1]), position[0]-(playpos[0]))
    playerrot = pygame.transform.rotate(slime, 360-angle*57.29)
    playerpos1 = (playpos[0]-playerrot.get_rect().width//2, playpos[1]-playerrot.get_rect().height//2)
    screen.blit(playerrot,playerpos1)

    position3 = pygame.mouse.get_pos()
    angle3 = math.atan2(position[1]-(playpos[1]), position3[0]-(playpos[0]))
    playerrot3 = pygame.transform.rotate(gun, 360-angle*59.24)
    playerpos13 = (playpos[0]-playerrot.get_rect().width//2-20, playpos[1]-playerrot3.get_rect().height//2)
    screen.blit(playerrot3,playerpos13)

    
    





    # 7. 화면을 다시 그린다.
    pygame.display.flip()





    # 8. 게임 종료
    for event in pygame.event.get():
        # 공격하기
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            acc[1] = acc[1] + 1
            bullets.append([math.atan2(position[1]-(playerpos13[1]), \
            position[0]-(playerpos13[0]+30)),playerpos13[0]+15,playerpos13[1]+30])
            
        if event.type == pygame.QUIT: # X를 눌렀을 때
            pygame.quit() # 게임 종료
            exit(0) # while문 탈출

        # 키보드를 눌렀을 때
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys[0] = True
            if event.key == pygame.K_a:
                keys[1] = True
            if event.key == pygame.K_s:
                keys[2] = True
            if event.key == pygame.K_d:
                keys[3] = True
        # 키보드를 떼었을 때
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            if event.key == pygame.K_a:
                keys[1] = False
            if event.key == pygame.K_s:
                keys[2] = False
            if event.key == pygame.K_d:
                keys[3] = False




    if keys[0]:
        playpos[1] = playpos[1] - 2
    if keys[2]:
        playpos[1] = playpos[1] + 2
    if keys[1]:
        playpos[0] = playpos[0] - 2
    if keys[3]:
        playpos[0] = playpos[0] + 2
