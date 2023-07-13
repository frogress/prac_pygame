import pygame
import sys

# 게임 창 크기 설정
screen_width = 800
screen_height = 600

# 버튼 클래스 정의
class Button:
    def __init__(self, x, y, width, height, idle_image, hover_image):
        self.rect = pygame.Rect(x, y, width, height)
        self.idle_image = idle_image
        self.hover_image = hover_image
        self.image = idle_image
        self.clicked = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.image = self.hover_image
            else:
                self.image = self.idle_image
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.clicked = False

# 게임 클래스 정의
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Empire Builder")
        self.clock = pygame.time.Clock()
        
        # 버튼 이미지 로드
        self.button_idle_img = pygame.image.load("resources/images/slimes.png").convert_alpha()
        self.button_hover_img = pygame.image.load("resources/images/slime_top.png").convert_alpha()
        
        # 버튼 생성
        button_width = 150
        button_height = 50
        button_x = (screen_width - button_width) // 2
        button_y = (screen_height - button_height) // 2
        self.button = Button(button_x, button_y, button_width, button_height, self.button_idle_img, self.button_hover_img)
        
    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                # 버튼 이벤트 처리
                self.button.handle_event(event)

            self.update()
            self.render()

        pygame.quit()
        sys.exit()
        
    def update(self):
        # 게임 상태 업데이트
        if self.button.clicked:
            print("버튼이 클릭되었습니다!")

    def render(self):
        # 게임 화면 그리기
        self.screen.fill((0, 0, 0))  # 검은색 배경
        self.button.draw(self.screen)  # 버튼 그리기
        pygame.display.flip()

# 게임 시작
game = Game()
game.run()