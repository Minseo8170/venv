import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 크기 및 설정
SCREEN_WIDTH, SCREEN_HEIGHT = 240, 240
BACKGROUND_WIDTH, BACKGROUND_HEIGHT = 1000, 240
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Castle Defence")

# 배경 이미지 로드
background = pygame.image.load('배경.png')
background_rect = background.get_rect()

# 배경 초기 위치 설정
x_offset = 240

# 캐릭터 아이콘 설정
character_icons = []
try:
    character_icons.append(pygame.image.load("1렙멍_기본.png").convert_alpha())
    character_icons.append(pygame.image.load("2렙멍_기본.png").convert_alpha())
    character_icons.append(pygame.image.load("3렙멍_기본.png").convert_alpha())
except pygame.error as e:
    print(f"이미지 로드 오류: {e}")
    sys.exit()

# 각 아이콘 크기 조정 (필요 시)
for i in range(len(character_icons)):
    character_icons[i] = pygame.transform.scale(character_icons[i], (60, 60))

# 상태 변수
selected_tab = 'background'
selected_background = 0
selected_icon = 1
last_spawn_time = {
    "Dog1" : 0,
    "Dog2" : 0,
    "Dog3" : 0
}
SPAWN_COOLDOWN = 4000

# 생성 캐릭터 관리 리스트
characters = []

# 적 캐릭터 관리 변수
enemy_last_spawn_time = {
    "Enemy1": 0,
    "Enemy2": 0
}
enemy_spawn_intervals = {
    "Enemy1": random.randint(5000, 10000),  # 초기화
    "Enemy2": random.randint(5000, 10000)
}


class Dog1:
    image_file_dog1_walk = [
        '1렙멍_걷기1.png',
        '1렙멍_걷기2.png',
        '1렙멍_걷기3.png',
        '1렙멍_걷기4.png',
    ]

    image_file_dog1_attack = [
        '1렙멍_공격1.png',
        '1렙멍_공격2.png',
        '1렙멍_공격3.png',
        '1렙멍_공격4.png',
        '1렙멍_공격5.png',
        '1렙멍_기본.png',
    ]

    def __init__(self, x, y):
        self.images = [pygame.image.load(img).convert_alpha() for img in self.image_file_dog1_walk]
        self.x = x
        self.y = y
        self.frame_index = 0
        self.speed = -2
        self.animation_time = 0

    # 캐릭터 이동 및 애니메이션 업데이트
    def update(self, dt):
        self.x += self.speed
        self.animation_time += dt
        repeated_frames = []
        if self.animation_time > 100: # 100ms마다 프레임 전환
            if self.frame_index == 1 or self.frame_index == 3:
                repeated_frames.extend([self.frame_index] * 7)
            self.frame_index = (self.frame_index + 1) % len(self.images)     
            self.animation_time = 0

    # 캐릭터 그리기
    def draw(self, surface):
        # 캐릭터를 중심 좌표에 맞게 보정
        character_rect = self.images[self.frame_index].get_rect(center=(self.x, self.y))
        surface.blit(self.images[self.frame_index], character_rect.topleft)

class Dog2:
    image_file_dog2_walk = [
        '2렙멍_걷기1.png',
        '2렙멍_걷기2.png',
        '2렙멍_걷기3.png',
        '2렙멍_걷기4.png',
    ]

    image_file_dog2_attack =[
        '2렙멍_공격1.png',
        '2렙멍_공격2.png',
        '2렙멍_공격3.png',
        '2렙멍_공격4.png',
        '2렙멍_공격5.png',
        '2렙멍_공격6.png',
        '2렙멍_기본.png',
    ]

    def __init__(self, x, y):
        self.images = [pygame.image.load(img).convert_alpha() for img in self.image_file_dog2_walk]
        self.x = x
        self.y = y
        self.frame_index = 0
        self.speed = -2
        self.animation_time = 0

    # 캐릭터 이동 및 애니메이션 업데이트
    def update(self, dt):
        self.x += self.speed
        self.animation_time += dt
        repeated_frames = []
        if self.animation_time > 100: # 100ms마다 프레임 전환
            if self.frame_index == 1 or self.frame_index == 3:
                repeated_frames.extend([self.frame_index] * 7)
            self.frame_index = (self.frame_index + 1) % len(self.images)     
            self.animation_time = 0

    # 캐릭터 그리기
    def draw(self, surface):
        # 캐릭터를 중심 좌표에 맞게 보정
        character_rect = self.images[self.frame_index].get_rect(center=(self.x, self.y))
        surface.blit(self.images[self.frame_index], character_rect.topleft)

class Dog3:
    image_file_dog3_walk = [
        '3렙멍_걷기1.png',
        '3렙멍_걷기2.png',
        '3렙멍_걷기3.png',
        '3렙멍_걷기4.png',
    ]

    image_file_dog3_attack = [
        '3렙멍_공격1.png',
        '3렙멍_공격2.png',
        '3렙멍_공격3.png',
        '3렙멍_공격4.png',
        '3렙멍_공격5.png',
        '3렙멍_공격6.png',
        '3렙멍_기본.png',
    ]
        
    def __init__(self, x, y):
        self.images = [pygame.image.load(img).convert_alpha() for img in self.image_file_dog3_walk]
        self.x = x
        self.y = y
        self.frame_index = 0
        self.speed = -2
        self.animation_time = 0

    # 캐릭터 이동 및 애니메이션 업데이트
    def update(self, dt):
        self.x += self.speed
        self.animation_time += dt
        repeated_frames = []
        if self.animation_time > 100: # 100ms마다 프레임 전환
            if self.frame_index == 1 or self.frame_index == 3:
                repeated_frames.extend([self.frame_index] * 7)
            self.frame_index = (self.frame_index + 1) % len(self.images)     
            self.animation_time = 0

    # 캐릭터 그리기
    def draw(self, surface):
        # 캐릭터를 중심 좌표에 맞게 보정
        character_rect = self.images[self.frame_index].get_rect(center=(self.x, self.y))
        surface.blit(self.images[self.frame_index], character_rect.topleft)

class enemy1:
    image_file_enemy1_walk = [
        '그라니_걷기1.png',
        '그라니_걷기2.png',
        '그라니_걷기3.png',
        '그라니_걷기4.png',
    ]

    image_file_enemy1_attack = [
        '그라니_공격1.png',
        '그라니_공격2.png',
        '그라니_공격3.png',
        '그라니_공격4.png',
        '그라니_공격5.png',
        '그라니_공격6.png',
        '그라니_공격7.png',
        '그라니_공격8.png',
        '그라니_기본.png',
    ]

    def __init__(self, x, y):
        self.images = [pygame.image.load(img).convert_alpha() for img in self.image_file_enemy1_walk]
        self.x = x
        self.y = y
        self.frame_index = 0
        self.speed = 2
        self.animation_time = 0

    # 캐릭터 이동 및 애니메이션 업데이트
    def update(self, dt):
        self.x += self.speed
        self.animation_time += dt
        repeated_frames = []
        if self.animation_time > 100: # 100ms마다 프레임 전환
            if self.frame_index == 1 or self.frame_index == 3:
                repeated_frames.extend([self.frame_index] * 7)
            self.frame_index = (self.frame_index + 1) % len(self.images)     
            self.animation_time = 0

    # 캐릭터 그리기
    def draw(self, surface):
        # 캐릭터를 중심 좌표에 맞게 보정
        character_rect = self.images[self.frame_index].get_rect(center=(self.x, self.y))
        surface.blit(self.images[self.frame_index], character_rect.topleft)

class enemy2:
    image_file_enemy2_walk = [
        '대지_걷기1.png',
        '대지_걷기2.png',
        '대지_걷기3.png',
        '대지_걷기4.png',
    ]

    image_file_enemy2_attack = [
        '대지_공격1.png',
        '대지_공격2.png',
        '대지_공격3.png',
        '대지_공격4.png',
        '대지_공격5.png',
        '대지_공격6.png',
        '대지_공격7.png',
        '대지_공격8.png',
        '대지_기본.png',
    ]

    def __init__(self, x, y):
        self.images = [pygame.image.load(img).convert_alpha() for img in self.image_file_enemy2_walk]
        self.x = x
        self.y = y
        self.frame_index = 0
        self.speed = 2
        self.animation_time = 0

    # 캐릭터 이동 및 애니메이션 업데이트
    def update(self, dt):
        self.x += self.speed
        self.animation_time += dt
        repeated_frames = []
        if self.animation_time > 100: # 100ms마다 프레임 전환
            if self.frame_index == 1 or self.frame_index == 3:
                repeated_frames.extend([self.frame_index] * 7)
            self.frame_index = (self.frame_index + 1) % len(self.images)     
            self.animation_time = 0

    # 캐릭터 그리기
    def draw(self, surface):
        # 캐릭터를 중심 좌표에 맞게 보정
        character_rect = self.images[self.frame_index].get_rect(center=(self.x, self.y))
        surface.blit(self.images[self.frame_index], character_rect.topleft)
        
class Enemy3:
    image_file_enemy3 = [
        '사자자리.jpg'
    ]

class Death:
    image_file_death = [
        '사망1.png'
        '사망2.png'
        '사망3.png'
        '사망4.png'
    ]

class Castle:
    castle = pygame.image.load('아군_성.png')

class Enemy_mt:
    enemy_mt = pygame.image.load('적_산.png')

# 메인 루프
clock = pygame.time.Clock()
while True:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if selected_tab == 'background':
        if keys[pygame.K_DOWN]:
            selected_tab = 'icon'
        elif keys[pygame.K_LEFT]:
            x_offset += 20
        elif keys[pygame.K_RIGHT]:
            x_offset -= 20
    else:
        if keys[pygame.K_UP]:
            selected_tab = 'background'
        elif keys[pygame.K_LEFT]:
            selected_icon = (selected_icon - 1) % 3
        elif keys[pygame.K_RIGHT]:
            selected_icon = (selected_icon + 1) % 3
        elif keys[pygame.K_a]:  # A 키를 누르면 캐릭터 생성
            if selected_icon == 0 and current_time - last_spawn_time["Dog1"] > SPAWN_COOLDOWN:  # 첫 번째 아이콘에 해당하는 Dog1 생성
                character_spawn_x = x_offset + 900
                character_spawn_y = 100  # Y축 정중앙 (240x240 캐릭터 기준으로 보정) 
                characters.append(Dog1(character_spawn_x, character_spawn_y))
                last_spawn_time["Dog1"] = current_time
            elif selected_icon == 1 and current_time - last_spawn_time["Dog2"] > SPAWN_COOLDOWN:  # 두 번째 아이콘에 해당하는 Dog2 생성
                character_spawn_x = x_offset + 900
                character_spawn_y = 100  # Y축 정중앙 (240x240 캐릭터 기준으로 보정) 
                characters.append(Dog2(character_spawn_x, character_spawn_y))
                last_spawn_time["Dog2"] = current_time
            elif selected_icon == 2 and current_time - last_spawn_time["Dog3"] > SPAWN_COOLDOWN:  # 세 번째 아이콘에 해당하는 Dog3 생성
                character_spawn_x = x_offset + 900
                character_spawn_y = 100  # Y축 정중앙 (240x240 캐릭터 기준으로 보정) 
                characters.append(Dog3(character_spawn_x, character_spawn_y))
                last_spawn_time["Dog3"] = current_time

    # 적 생성 로직
    for enemy_type in ["Enemy1", "Enemy2"]:
        if current_time - enemy_last_spawn_time[enemy_type] > enemy_spawn_intervals[enemy_type]:
            spawn_x = x_offset + 50
            spawn_y = 100
            if enemy_type == "Enemy1":
                characters.append(enemy1(spawn_x, spawn_y))
            elif enemy_type == "Enemy2":
                characters.append(enemy2(spawn_x, spawn_y))
            
            # 스폰 시간 및 다음 간격 갱신
            enemy_last_spawn_time[enemy_type] = current_time
            enemy_spawn_intervals[enemy_type] = random.randint(2000, 5000)

    # 배경 위치 조정
    x_offset = max(min(x_offset, 0), SCREEN_WIDTH - background_rect.width)
    
    # 배경 그리기
    screen.blit(background, (x_offset, 0))

    #아군 성, 적 산 그리기
    screen.blit(Castle.castle, (x_offset + 900, 15))
    screen.blit(Enemy_mt.enemy_mt, (x_offset, 15))

    # 캐릭터 업데이트 및 그리기
    for character in characters:
        character.update(dt)
        character.draw(screen)

    # 캐릭터 아이콘 영역 그리기
    for i in range(3):
        rect = pygame.Rect(i * 80, SCREEN_HEIGHT - 60, 80, 80)
        if i == selected_icon:
            pygame.draw.rect(screen, (255, 0, 0), rect, 3)
        else:
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)
        screen.blit(character_icons[i], rect.topleft)

    pygame.display.flip()
    dt = clock.tick(15)
