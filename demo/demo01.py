import os
import re
import pyautogui  # PyAutoGUIをインポート
from pygame import mixer  # pygameライブラリを使用してmp3を再生

# 指定されたディレクトリ内の.mp3ファイル一覧を取得
folder_path = 'audio/Word2Motion'
print(os.listdir(folder_path))
files = [file for file in os.listdir(folder_path) if file.endswith('.wav')]
print(files)

emotion_to_number = {
    "reset": 0,
    "joy": 1,
    "angry": 2,
    "sorrow": 3,
    "fun": 4,
    "wave": 5,
    "good": 6,
    "nodding": 7,
    "shaking": 8,
    "clap": 9
}

# ファイル名を基にソートするための関数
def sort_files(file):
    # ファイル名から数字を抽出
    number = re.search(r'\d+', file)
    if number:
        return int(number.group())
    return 0

# ファイルを数字の順番にソート
sorted_files = sorted(files, key=sort_files)

# pygameのmixerモジュールを初期化
mixer.init()

# ソートされたファイルを順番に再生
for file in sorted_files:
    # ファイルのフルパスを取得
    file_path = os.path.join(folder_path, file)
    # ファイル名から感情を抽出
    emotion = file.split('_')[-1].split('.')[0]
    print(f"再生中: {file} - 感情: {emotion} [{emotion_to_number[emotion]}]")
    
    # 再生完了後、対応する感情の番号を自動でキーボード入力
    pyautogui.typewrite(str(emotion_to_number[emotion]))
    # pyautogui.press('enter')  # 必要に応じてEnterキーを押す

    # ファイルを再生
    mixer.music.load(file_path)
    mixer.music.play()
    
    # ファイルの再生が完了するのを待つ
    while mixer.music.get_busy():
        continue

