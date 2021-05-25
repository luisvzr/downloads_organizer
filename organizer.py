import os
import shutil


source = input("Please insert your Downloads full folder path:\n")
root_path = "E:/Share/"

app_folder = "Downloads/Installers"
music_folder = "Music"
pictures_folder = "Pictures"
video_folder = "Movies&Series"
compressed_folder = "Downloads/Compressed"
docs_folder = "Documents"
isos_folder = "ISOS"
subs_folder = "Subs"

dictionary = {
    app_folder: (".exe", ".msi"),
    music_folder: (".mp3", ".m4a"),
    pictures_folder: (".jpg", ".png"),
    video_folder: (".mp4", ".mkv"),
    compressed_folder: (".zip", ".rar", ".ZIP"),
    docs_folder: (".pdf", ".doc", ".docx", ".xls"),
    isos_folder: ".iso"
}

def create(dir):
    dir_name = "E:/Share/%s" % (dir)
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        pass

def move_file(file,dir):
    dest = str(root_path + dir +"/"+ file)
    src = str(source+ "/" + file)
    shutil.move(src , dest)
    print("[MOVING] %s/%s" % (dir, file))

for f in os.listdir(source):
    for dir in dictionary:
        create(dir)
        if f.endswith(dictionary[dir]):
            move_file(f,dir)
