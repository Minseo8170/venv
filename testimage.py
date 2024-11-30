from PIL import Image

gif = Image.open('6a60c19a12789ba5.gif')

# GIF 프레임 개수 확인
frame_count = 0
try:
    while True:
        gif.seek(gif.tell() + 1)
        frame_count += 1
except EOFError:
    pass

print("GIF 프레임 개수:", frame_count)
