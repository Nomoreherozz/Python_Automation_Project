#! E:\Python Learing\Automation Script\env\Scripts\python.exe

#Import Libraries
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

#Get your youtube video URL and select the format and resoolution
def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded Successfully")
    except Exception as e:
        print(e)

#Create UI for the tools
def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder

#Prevent module being used by other python file
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

#Ask for URL Input and Save path then started download
    video_url = input("Please enter a YouTube URL: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download... ")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")

