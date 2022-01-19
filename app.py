import time
from TikTokApi import TikTokApi
from moviepy.editor import *
from pathlib import Path
import os

os.chdir(os.getcwd()) # Change Directory to Current working directory
file_path = "downloads" # Define file_path

# Unofficial Tiktok Api
api = TikTokApi.get_instance()
results = 30
tiktoks = api.by_hashtag('funny', count=results, custom_verifyFp="")

Path("downloads").mkdir(exist_ok=True) # Create "DOWNLOADS" directory 
print("donwload folder created")
# The loop below downloads the video in the "file_path" folder
for i in range(len(tiktoks)):
    data = api.get_video_by_tiktok(tiktoks[i])
    with open(file_path+"/{}.mp4".format(str(i)), 'wb') as output:
        output.write(data)
    print(f"{i+1} downloaded")
    
print(f"download complete \n Compiling videos...")
# Append each video to "CLIPS"array using the loop below
clips = []
for num in range(results):
    clip = VideoFileClip(f"{file_path}/{num}.mp4")
    clips.append(clip)

# Compile videos
final_clip = concatenate_videoclips(clips, method='compose')
final_clip.write_videofile(
    "TiktokYoutube.mp4", 
    temp_audiofile='temp-audio.m4a', 
    remove_temp=True, 
    codec="libx264", 
    audio_codec="aac")

time.sleep(5) # Stop program for 5 seconds

os.system('python upload_video.py --file="TiktokYoutube.mp4" --title="TOP 30 Trending TIK TOK MEMES" --description="TOP 30 Trending TIK TOK MEMES🤣\n\n❤️Subscribe For Daily TikTok Videos\n👍Drop a LIKE for MORE TikTok Compilations\n🔔Turn on the bell to know whenever I uploads" --keywords="tiktok,meme,funny" --category="22" --privacyStatus="private"') # Execute upload_video.py command