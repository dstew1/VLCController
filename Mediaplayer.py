import time
import subprocess
from pathlib import Path

# Use the vlc command line tool to control the media player
vlc = Path("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")

# The video to be played
video = Path("C:\\Mediaplayer\\video.mp4")

# Start playing the video
player = subprocess.Popen([vlc, video])

# This loop will run until the user presses q to quit
while True:
    # Prompt the user for an input
    prompt = input("Press a number 0-9 to jump to the corresponding seconds in the video, or press q to quit: ")

    # If the user presses q, quit the loop
    if prompt == "q":
        break

    # If the user presses a number 0-9, jump to the corresponding second
    elif prompt in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        # Use the VLC command line tool to jump to the specified second
        player.terminate()
        player = subprocess.Popen([vlc, "--start-time", prompt + "s", video])
        time.sleep(2)

# Quit the VLC media player
player.terminate()
