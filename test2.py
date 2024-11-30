import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 크기 설정
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("이미지 애니메이션")

# 배경 이미지 로드
background = pygame.image.load('image_sample.png')
background_rect = background.get_rect()

# 애니메이션 이미지 로드
# 이미지 파일 경로 리스트
image_files_dog1 = [
    "1렙멍_걷기1.png",
    "1렙멍_걷기2.png",
    "1렙멍_걷기2.png",
    "1렙멍_걷기2.png",
    "1렙멍_걷기2.png",
    "1렙멍_걷기2.png",
    "1렙멍_걷기2.png",
    "1렙멍_걷기2.png",
    "1렙멍_걷기3.png",
    "1렙멍_걷기4.png",
    "1렙멍_걷기4.png",
    "1렙멍_걷기4.png",
    "1렙멍_걷기4.png",
    "1렙멍_걷기4.png",
    "1렙멍_걷기4.png",
    "1렙멍_걷기4.png",
    "1렙멍_공격1.png",
    "1렙멍_공격2.png",
    "1렙멍_공격3.png",
    "1렙멍_공격3.png",
    "1렙멍_공격3.png",
    "1렙멍_공격4.png",
    "1렙멍_공격5.png",
    "1렙멍_공격5.png",
    "1렙멍_공격5.png",
    "1렙멍_공격5.png",
    "1렙멍_공격5.png",
    "1렙멍_공격5.png",
    "1렙멍_공격5.png",
    "1렙멍_공격5.png",
    "1렙멍_공격5.png",
]

image_files_dog2 = [
    "2렙멍_걷기1.png",
    "2렙멍_걷기2.png",
    "2렙멍_걷기2.png",
    "2렙멍_걷기2.png",
    "2렙멍_걷기2.png",
    "2렙멍_걷기2.png",
    "2렙멍_걷기2.png",
    "2렙멍_걷기2.png",
    "2렙멍_걷기3.png",
    "2렙멍_걷기4.png",
    "2렙멍_걷기4.png",
    "2렙멍_걷기4.png",
    "2렙멍_걷기4.png",
    "2렙멍_걷기4.png",
    "2렙멍_걷기4.png",
    "2렙멍_걷기4.png",
    "2렙멍_공격1.png",
    "2렙멍_공격2.png",
    "2렙멍_공격3.png",
    "2렙멍_공격3.png",
    "2렙멍_공격3.png",
    "2렙멍_공격4.png",
    "2렙멍_공격5.png",
    "2렙멍_공격6.png",
    "2렙멍_공격6.png",
    "2렙멍_공격6.png",
    "2렙멍_공격6.png",
    "2렙멍_공격6.png",
    "2렙멍_공격6.png",
    "2렙멍_공격6.png",
    "2렙멍_공격6.png",
    "2렙멍_공격6.png",
]

image_files_dog3 = [
    "3렙멍_걷기1.png",
    "3렙멍_걷기2.png",
    "3렙멍_걷기2.png",
    "3렙멍_걷기2.png",
    "3렙멍_걷기2.png",
    "3렙멍_걷기2.png",
    "3렙멍_걷기2.png",
    "3렙멍_걷기2.png",
    "3렙멍_걷기3.png",
    "3렙멍_걷기4.png",
    "3렙멍_걷기4.png",
    "3렙멍_걷기4.png",
    "3렙멍_걷기4.png",
    "3렙멍_걷기4.png",
    "3렙멍_걷기4.png",
    "3렙멍_걷기4.png",
    "3렙멍_공격1.png",
    "3렙멍_공격2.png",
    "3렙멍_공격2.png",
    "3렙멍_공격3.png",
    "3렙멍_공격4.png",
    "3렙멍_공격5.png",
    "3렙멍_공격6.png",
    "3렙멍_공격6.png",
    "3렙멍_공격6.png",
    "3렙멍_공격6.png",
    "3렙멍_공격6.png",
    "3렙멍_공격6.png",
    "3렙멍_공격6.png",
]

image_files_death = [
    "사망1.png",
    "사망2.png",
    "사망3.png",
    "사망4.png",
]

# 이미지를 Pygame 객체로 변환
animation_frames_dog1 = [pygame.image.load(img1) for img1 in image_files_dog1]
animation_frames_dog2 = [pygame.image.load(img2) for img2 in image_files_dog2]
animation_frames_dog3 = [pygame.image.load(img3) for img3 in image_files_dog3]
animation_frames_death = [pygame.image.load(img4) for img4 in image_files_death]

# 프레임 지속 시간 (ms 단위, 모든 프레임 동일하게 설정)
frame_duration = 100
frame_index = 0
frame_index2 = 0
frame_index3 = 0
frame_index4 = 0
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

    # 배경 그리기
    screen.blit(background, (x_offset, y_offset))

    # 현재 프레임 그리기
    if animation_frames_dog1:
        screen.blit(animation_frames_dog1[frame_index], (object_x, object_y))

    if animation_frames_dog2:
        screen.blit(animation_frames_dog2[frame_index2], (object_x+100, object_y))

    if animation_frames_dog3:
        screen.blit(animation_frames_dog3[frame_index3], (object_x-100, object_y))

    if animation_frames_death:
        screen.blit(animation_frames_death[frame_index4], (object_x-200, object_y))

    # 시간 누적 및 프레임 업데이트
    time_accumulator += clock.get_time()
    if time_accumulator >= frame_duration:
        time_accumulator = 0
        frame_index = (frame_index + 1) % len(animation_frames_dog1)
        frame_index2 = (frame_index2 + 1) % len(animation_frames_dog2)
        frame_index3 = (frame_index3 + 1) % len(animation_frames_dog3)
        frame_index4 = (frame_index4 + 1) % len(animation_frames_death)

    # 화면 업데이트
    pygame.display.flip()

    # 프레임 속도 조절
    clock.tick(15)  # 최대 60FPS
