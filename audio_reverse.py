import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

from pydub import AudioSegment

folder_path="C:\Users\kevin_rkz3370\Desktop\song"

# 設定資料夾路徑
if len(sys.argv) == 2:
    folder_path = sys.argv[1]
elif len(folder_path) == "":
    print("請輸入資料夾路徑。")
    exit()


if not os.path.isdir(folder_path):
    print("資料夾不存在，請確認路徑是否正確。")
    exit()

mp3_files = [f for f in os.listdir(folder_path) if f.endswith('正放.mp3')]

for file_name in mp3_files:
    file_path = os.path.join(folder_path, file_name)

    audio = AudioSegment.from_mp3(file_path)
    reversed_audio = audio.reverse()
    
    #換成倒放.mp3
    reversed_file_name = f"{file_name[:-6]}倒放.mp3"
    reversed_file_path = os.path.join(folder_path, reversed_file_name)
    reversed_audio.export(reversed_file_path, format="mp3")

    print(f"[{file_name}]已反轉並另存為[{reversed_file_name}]")

print("所有 mp3 檔案已反轉完成。")
