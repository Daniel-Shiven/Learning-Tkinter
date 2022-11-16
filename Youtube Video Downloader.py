from os import path
from tkinter import *
from tkinter import filedialog

import shutil #allows us to copy files/folders and move them

#Have to be installed on terminal (pip install)
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import *

#Functions
def download():
    progress.config(text="Downloading")
    global path
    #Allows user to select a path
    user_path = ''
    user_path = filedialog.askdirectory()
    print(user_path)

    if user_path != "":
        #Remove link from entry box, set link as a variable
        video_link = link_entry.get()
        link_entry.config(text="")

        #download video
        mp4_video = YouTube(video_link).streams.get_highest_resolution().download()
        vid_clip = VideoFileClip(mp4_video)
        vid_clip.close()

        #Move file to selected directory
        shutil.move(mp4_video, user_path)
        progress.config(text="All Done! Download Another File")
    else:
        progress.config(text='')


#Create window
root = Tk()
title = root.title("Youtube Video Downloader")


#Create canvas for logo
downloader = Canvas(root, width=400,height=500)
downloader.grid(row=0,column=0)

#Image logo
logo_img = PhotoImage(file='ytlogo.png')

logo_img = logo_img.subsample(3, 3)

downloader.create_image(200, 125, image=logo_img)


#Link Field
link_label = Label(root, text="Enter Video Link:",font=('Comic Sans MS',17,'bold'),pady=5)
link_entry = Entry(root, width=45 ,bd=2,font=('Helvetica', 11))

#Add widgets to window
downloader.create_window(200, 260, window=link_label)
downloader.create_window(200, 300, window=link_entry)

#Download btns
download_btn = Button(root, text="Download", font=('Comic Sans MS', 17),bg='#0C88AB', command=download)
progress = Label(root, text="",font=('Comic Sans MS', 15))

#Add to Canvas
downloader.create_window(200, 350, window=download_btn)
downloader.create_window(200, 400, window=progress)


root.mainloop()