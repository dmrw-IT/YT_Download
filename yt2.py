#!/usr/bin/python3

import os, os.path, sys
from pytube import YouTube
from pytube import Playlist

##### TO DO: #####

### : Implement Playlists
# 2 : Implement Progress Bars
# 3 : Implement "Get Latest Video from a Channel"
# 4 : Provide support for Windows and MacOS
# 5 : In clean_string function, implement REGEX to filter characters in Video titles
# 6 : Figure out how to carry the cleaned "filename" all the way to the output file
# 7 : Error Handling for a bad URL
### : Implement Exit ability into user inputs

# V_Test_URL 1: https://www.youtube.com/watch?v=41rHu8rlvTI
# V_Test_URL 2: https://www.youtube.com/watch?v=ssvdczn-9qQ
# P_Test_URL: https://www.youtube.com/playlist?list=PLlQRht9pdQyQBqKt-5wuuKoZ7ohJ5A1Y5

##### Functions #####

# Strip certain characters out of Title used for Filename:
def clean_string(title_string):
    elim_dict = {"|":"", " ":"_", "'":"" }
    table = title_string.maketrans(elim_dict)
    title_string = title_string.translate(table)
    
# Function to handle downloading single YT Video:
def video():
    # Prompt User to provide a YT Video link:
    url = input('Enter the YT Video link you would like to download: ')
    
    # Set Variable for YouTube object:
    yt = YouTube(url)

    # Set Output File path for current Linux user:
    yt_dir = "/YT_Downloads/videos/"
    full_path = os.path.expanduser('~') + yt_dir
    if not os.path.exists(full_path):
        os.mkdir(full_path)

    # Get the Title of the Video:
    title = yt.title
    clean_string(title)

    # Target Stream by itag(22). This itag generally Progressive and 720p resolution:
    # See PyTube documentation for more information about Streams and StreamQueries #
    stream = yt.streams.get_by_itag(22)

    # Download the video:
    print(f"Downloading: {yt.title}")
    stream.download(output_path=full_path, filename=title)
    
    print("\nDownload Complete: Restarting the Program...\n")

# Function to handle downloading YT Playlist:
def playlist():

    # Prompt User to provide a YT Playlist link:
    url = input('Enter the YT Playlist link you would like to download: ')

    # Set Variable for Playlist object:
    p = Playlist(url)

    # Create proper directory paths if they don't already exist:
    p_dir = "/YT_Downloads/playlists/"
    full_path = os.path.expanduser('~') + p_dir
    if not os.path.exists(full_path):
        os.mkdir(full_path)

    # Get the Title of the Playlist:
    title = p.title
    clean_string(title)

    # Handling Single Video title output for video/p.video for loop:
    video_links = p.video_urls
    video_titles = []
    vl_count = 0
    for link in video_links:
        video_titles.append(YouTube(link).title)

    print(f"Downloading Playlist: {title}\n")

    # Loop that handles Playlist Download:
    for video in p.videos:
        print(f"Downloading: {video_titles[vl_count]}")
        video.streams.get_by_itag(22).download(output_path=full_path)
        vl_count += 1

    print("\nDownload Complete: Restarting the Program...\n")
                
def exit_program(counter, main):
    # Handle Exit logic: Counter reaches 5, Exit Program.
    if counter == 5:
        print(f"{counter}/5 attempts remaining...")
        main = False
        print("Exiting Program: Too Many Errors. Thank you for using YT_Download.")
        sys.exit()
    # main set to False, Exit Program:
    elif main == False:
        print("Thank you for using YT_Download")
        sys.exit()
    
class my_exception(Exception):
    pass

##### Main #####
user_choice = [1,2,3]
counter = 0
main = True

print("YT_Download: A program to download single YT Videos, or full Playlists.")

while main == True:

    try:

        v_or_p = int(input('Choose 1 for Video, or 2 for Playlist or 3 to exit the program: '))

        if v_or_p in user_choice and v_or_p == 1:
            video()      
            
        elif v_or_p in user_choice and v_or_p == 2:
            playlist()
            
        elif v_or_p in user_choice and v_or_p == 3:
            main = False

        else: 
            raise my_exception(v_or_p)

    except my_exception as e:
        print(f"{e} is greater than 2, make sure to enter a 1 for Video or 2 for Playlist or 3 to exit the program.")
        counter += 1
        exit_program(counter)
        
    except:
        print("Make sure to enter a 1 for Video or a 2 for Playlist or 3 to exit the program.")
        counter += 1
        exit_program(counter)

exit_program(counter, main)
