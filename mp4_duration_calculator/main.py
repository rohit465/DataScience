import os
from moviepy import VideoFileClip

def get_total_video_duration(folder_path):
    total_duration = 0.0
    for file_name in os.listdir(folder_path):
        if file_name.endswith(('.mkv', '.mp4')):
            video_path = os.path.join(folder_path, file_name)
            try:
                print(f"FileName: {file_name}")
                video = VideoFileClip(video_path)
                total_duration += video.duration
                video.close()
            except Exception as e:
                print(f"Could not procedd Vide {file_name}")

    hour = int(total_duration // 3600)
    minutes = int((total_duration % 3600)//60)
    seconds = int(total_duration % 60)
    
    return f"Hours: {hour} : Minutes: {minutes} : Seconds: {seconds}"



print(get_total_video_duration("D:\Downloads\Telegram\SpringBoot"))