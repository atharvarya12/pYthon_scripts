import os
import shutil
import time

download_folder = "C:/Users/athar/Downloads"
destination_folders = {
    'images': "C:/Users/athar/Downloads/pictures",
    'documents': "C:/Users/athar/Downloads/documents",
    'videos': "C:/Users/athar/Downloads/videos",
    'music': "C:/Users/athar/Downloads/musics",
    'others': "C:/Users/athar/Downloads/others"
}

file_types = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt'],
    'videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov'],
    'music': ['.mp3', '.wav', '.aac', '.flac'],
    'others': []
}

def move_file(file_name):
    file_extension = os.path.splitext(file_name)[1].lower()
    moved = False

    for category, extensions in file_types.items():
        if file_extension in extensions:
            destination = destination_folders[category]
            shutil.move(os.path.join(download_folder, file_name), os.path.join(destination, file_name))
            moved = True
            print(f"Moved {file_name} to {destination}")
            break

    if not moved:
        destination = destination_folders['others']
        shutil.move(os.path.join(download_folder, file_name), os.path.join(destination, file_name))
        print(f"Moved {file_name} to {destination_folders['others']}")

def monitor_folder():
    while True:
        for file_name in os.listdir(download_folder):
            file_path = os.path.join(download_folder, file_name)
            if os.path.isfile(file_path):
                move_file(file_name)
        time.sleep(10)  # Wait for 10 seconds before checking again

if __name__ == "__main__":
    monitor_folder()
