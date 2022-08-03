#!/usr/bin/python3

import os, os.path, sys
from pytube import YouTube
from pytube import Playlist

######
# 1 : Implement Playlists
# 2 : Implement Progress Bars
# 3 : Implement "Get Latest Video from a Channel"
# 4 : Provide support for Windows and MacOS
# 5 : In clean_string function, implement REGEX to filter characters in Video titles
# 6 : Figure out how to carry the cleaned "filename" all the way to the output file


# P_Test_URL: https://www.youtube.com/playlist?list=PLlQRht9pdQyQBqKt-5wuuKoZ7ohJ5A1Y5

# Functions

# CLEAN_STRING() : Strip certain characters out of Title used for Filename:
### Future Implementation: REGEX ###
def clean_string(title_string):
    elim_dict = {"|":"", " ":"_", "'":"" }
    table = title_string.maketrans(elim_dict)
    title_string = title_string.translate(table)
    print (title_string)

def video():
                # Prompt User to provide a YouTube Video link:
                url = input('Enter the YouTube Video link you would like to download: ')
                # Set Variable for YouTube object:
                yt = YouTube(url)
                # Set Output File path for current Linux user:
                ### Future Implementation: Incorporate ALL operating systems ###
                yt_dir = "/YT_Downloads/"
                full_path = os.path.expanduser('~') + yt_dir

                if not os.path.exists(full_path):
                    os.mkdir(full_path)

                # Get the Title of the video and replace the spaces with underscores:
                title = yt.title

                clean_string(title)

                # Target a Stream that is Progressive and has 720p resolution:
                stream = yt.streams.get_by_itag(22)

                # Download the video:
                stream.download(output_path=full_path, filename=title)

def counter_to_exit(counter):
    print(f"{counter}/5 attempts remaining...")
    if counter == 5:
        bool_cond = False
        print("Too many errors, exiting program.")
        sys.exit()

class my_exception(Exception):
    pass

######## Main #########

user_choice = [1,2]
counter = 0
bool_cond = True

print("YT_Download: A program to download single YT Videos, or full Playlists.")

while bool_cond == True:

    try:

        v_or_p = int(input('Choose 1 for Video, or 2 for Playlist: '))

        if v_or_p in user_choice and v_or_p == 1:
            video()
            
        elif v_or_p in user_choice and v_or_p == 2:
            print("Playlist") 
            break 

        else: 
            raise my_exception(v_or_p)

    except my_exception as e:
        print(f"{e} is greater than 2, make sure to enter a 1 for Video or 2 for Playlist.")
        counter += 1
        counter_to_exit(counter)
        
    
    except:
        print("Make sure to enter a 1 for Video or a 2 for Playlist.")
        counter += 1
        counter_to_exit(counter)

print("game over")
