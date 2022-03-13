from pytube import YouTube
import moviepy.editor 
import os ,time

while(True):
    os.system("cls")
    
    # 要檢查的檔案路徑
    video_folder = "./video"
    audio_folder = "./audio"

    # 檢查檔案是否存在
    if os.path.isfile(video_folder):
        os.mkdir("./video")
        print("建立資料夾: video")
    if os.path.isfile(audio_folder):
        os.mkdir("./audio")
        print("建立資料夾: audio")

    #定義下載 Youtube 檔案
    url = str(input("請貼上 Youtube 影片連結(輸入 EXIT 結束):　"))
    if(url == "EXIT"):
        break
    file = str(input("請輸入名稱:　"))

    #宣告 pytube 函式值
    yt = YouTube(url)

    print("開始下載影片")
    yt.streams.get_highest_resolution().download("./video" ,filename = file + ".mp4")
    print("影片下載完成")
    time.sleep(0.5)
    os.system("cls")

    print("開始轉換檔案")
    video = moviepy.editor.VideoFileClip("./video/" + file + ".mp4")
    video.audio.write_audiofile("./audio/" + file + ".mp3")
    print("檔案轉換完成")
    time.sleep(0.5)
    os.system("cls")
