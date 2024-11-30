import pygame
import sys

# 초기화
pygame.init()

# 화면 크기 및 설정
SCREEN_WIDTH, SCREEN_HEIGHT = 240, 240
BACKGROUND_WIDTH = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("냥코대전쟁 유사 게임")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SELECTED_BORDER_COLOR = (255, 0, 0)

# 캐릭터 아이콘 및 배경 설정
character_icons = [pygame.Surface((80, 80)) for _ in range(3)]
for icon in character_icons:
    icon.fill((0, 255, 0))  # 아이콘 색상 (초록색)

background_image = pygame.Surface((BACKGROUND_WIDTH, SCREEN_HEIGHT))
background_image.fill((0, 0, 255))  # 배경색 (파란색)

# 상태 변수
selected_tab = 'background'  # 'background' or 'character'
background_offset = 0
selected_character = 1  # 가운데 캐릭터 아이콘 선택

# 메인 루프
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if selected_tab == 'background':
        if keys[pygame.K_UP]:
            selected_tab = 'character'
        elif keys[pygame.K_LEFT]:
            background_offset = max(0, background_offset - 1)  # 왼쪽으로 이동
        elif keys[pygame.K_RIGHT]:
            background_offset = min(BACKGROUND_WIDTH - SCREEN_WIDTH, background_offset + 1)  # 오른쪽으로 이동
    else:  # selected_tab == 'character'
        if keys[pygame.K_DOWN]:
            selected_tab = 'background'
        elif keys[pygame.K_LEFT]:
            selected_character = (selected_character - 1) % 3  # 왼쪽 아이콘으로 이동
        elif keys[pygame.K_RIGHT]:
            selected_character = (selected_character + 1) % 3  # 오른쪽 아이콘으로 이동

    # 화면 그리기
    screen.fill(WHITE)

    # 배경 그리기
    screen.blit(background_image, (-background_offset, 0))

    # 캐릭터 아이콘 영역 그리기
    for i in range(3):
        rect = pygame.Rect(i * 80, SCREEN_HEIGHT - 80, 80, 80)
        if i == selected_character:
            pygame.draw.rect(screen, SELECTED_BORDER_COLOR, rect, 3)
        else:
            pygame.draw.rect(screen, BLACK, rect, 1)
        screen.blit(character_icons[i], rect.topleft)

    pygame.display.flip()
    clock.tick(60)
