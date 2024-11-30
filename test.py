import pygame
import sys
from PIL import Image

# Pygame 초기화
pygame.init()

# 화면 크기 설정
SCREEN_WIDTH = 240
SCREEN_HEIGHT = 240
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("간단한 게임")

# 배경 이미지 로드
background = pygame.image.load('image_sample.png')
background_rect = background.get_rect()

# GIF 파일 열기
gif = Image.open('6a60c19a12789ba5.gif')  # GIF 파일 경로

# 프레임 리스트 생성
pygame_frames = []
frame_durations = []

try:
    while True:
        frame = gif.copy().convert("RGBA")  # 프레임 복사 및 RGBA 변환
        pygame_frame = pygame.image.fromstring(frame.tobytes(), frame.size, "RGBA")
        pygame_frame = pygame.transform.scale(pygame_frame, (90, 80))  # 크기 조정
        pygame_frames.append(pygame_frame)
        frame_durations.append(gif.info.get("duration", 100))  # 프레임 지속 시간(ms)
        gif.seek(gif.tell() + 1)  # 다음 프레임으로 이동
except EOFError:
    pass  # 모든 프레임 처리 완료

# 애니메이션 변수
frame_index = 0
clock = pygame.time.Clock()
time_accumulator = 0  # 시간 누적 변수

# 초기 위치 설정
x_offset = 0
y_offset = 0

# 초기 위치 설정
object_x = SCREEN_WIDTH // 2 - 30
object_y = SCREEN_HEIGHT // 2 - 40

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 키 입력 처리
    keys = pygame.key.get_pressed()

    # 방향키 조작
    if keys[pygame.K_LEFT]:
        x_offset += 30
    if keys[pygame.K_RIGHT]:
        x_offset -= 30
    if keys[pygame.K_UP]:
        y_offset += 30
    if keys[pygame.K_DOWN]:
        y_offset -= 30

    # 배경 위치 조정
    x_offset = max(min(x_offset, 0), SCREEN_WIDTH - background_rect.width)
    y_offset = max(min(y_offset, 0), SCREEN_HEIGHT - background_rect.height)

    # 화면 색상 채우기
    screen.fill(BLACK)

    # 배경 그리기
    screen.blit(background, (x_offset, y_offset))

    # 현재 프레임 그리기
    if pygame_frames:  # 프레임 리스트가 비어있지 않으면 그리기
        screen.blit(pygame_frames[frame_index], (object_x, object_y))  # 객체 위치에 그리기

    # 시간 누적 및 프레임 업데이트
    time_accumulator += clock.get_time()
    if time_accumulator >= frame_durations[frame_index]:
        time_accumulator = 0
        frame_index = (frame_index + 1) % len(pygame_frames)

    # 화면 업데이트
    pygame.display.flip()

    # 프레임 속도 조절
    clock.tick(60)  # 최대 60FPS
