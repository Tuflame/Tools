import os
import sys
import pygame

sys.stdout.reconfigure(encoding='utf-8')

# 初始化 pygame
pygame.mixer.init()

folder_path = "C:/Users/kevin_rkz3370/Desktop/song"

# 檢查資料夾是否存在
if not os.path.isdir(folder_path):
    print("資料夾不存在，請確認路徑是否正確。")
    exit()

# 獲取資料夾內所有的 mp3 文件
mp3_files = [f for f in os.listdir(folder_path) if f.endswith('.mp3')]

if not mp3_files:
    print("資料夾中沒有 mp3 文件。")
    exit()

# 初始化 pygame 的顯示，用於捕捉按鍵事件
pygame.display.init()
window = pygame.display.set_mode((400, 200))  # 必須設置一個窗口

# 設置按鍵重複，這樣可以確保按住按鍵時不會漏掉事件
pygame.key.set_repeat(500, 50)

count = 0

for file_name in mp3_files:
    count += 1
    # 加載音樂文件
    pygame.mixer.music.load(os.path.join(folder_path, file_name))
    print(f"第{count}首 : {file_name[:-4]}")
    
    # 開始播放音樂
    pygame.mixer.music.play()
    
    # 等待播放，按下空白鍵跳過或繼續下一首
    playing = True
    while playing and pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(f"捕捉到按鍵: {event.key}")  # 調試輸出，檢查按鍵事件是否被捕捉
                if event.key == pygame.K_SPACE:  # 按空白鍵跳過
                    pygame.mixer.music.stop()
                    playing = False

    # 提示用戶按下空白鍵播放下一首
    print("按下空白鍵播放下一首")
    
    waiting_for_next = True
    while waiting_for_next:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(f"捕捉到按鍵: {event.key}")  # 調試輸出，檢查按鍵事件是否被捕捉
                if event.key == pygame.K_SPACE:  # 按下空白鍵播放下一首
                    waiting_for_next = False

# 結束 pygame
pygame.quit()
