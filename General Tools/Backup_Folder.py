import os
import shutil
import datetime
import schedule
import time

#Define source folder path and destination folder path
source_dir = "E:/Internship"
destination_dir = "D:/BACK UP/Internship_back_ups"

#Function to back up folder with date stamp as name
def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try: 
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in {dest}")

#Make a schedule to run this script everyday at a time you choose
schedule.every().day.at("20:04").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)


    