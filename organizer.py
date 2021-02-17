import os
import shutil

# Archivos de downloads:
print("Please insert your Downloads folder path:")
source = input()
#source = "E:/Share/Downloads"
files = os.listdir(source)

# tuples
pictures = (".jpg", ".png")
music = (".mp3", ".m4a")
video = (".mp4", ".mkv")
app = (".exe", ".msi")
compressed = (".zip", ".rar", ".ZIP")
docs = (".pdf", ".doc", ".docx", ".xls")
isos = ".iso"

# folders:
root_path = "E:/Share/"

app_folder = "Downloads/Installers"
music_folder = "Music"
pictures_folder = "Pictures"
video_folder = "Movies&Series"
compressed_folder = "Downloads/Compressed"
docs_folder = "Documents"
isos_folder = "ISOS"
subs_folder = "Subs"



folders = [app_folder, music_folder, pictures_folder, video_folder, compressed_folder, docs_folder, subs_folder]

for folder in folders:
    isFile = os.path.isfile(os.path.join(root_path,folder))
    if isFile == True:
        print(folder, " Exist")
    else:    
        os.makedirs(os.path.join(root_path,folder),exist_ok=True)  

for f in files:
    #print(str(root_path+music_folder+"/"+f))
    if f.endswith(tuple(music)):
        shutil.move(source+ "/" + f,(str(root_path+music_folder+"/"+f)))
        print(f, "moved succesfully!")
    elif f.endswith(tuple(pictures)):
        shutil.move(source + "/" + f,(str(root_path+pictures_folder+"/"+f)))
        print(f, "moved succesfully!")
    elif f.endswith(tuple(compressed)):
        shutil.move(source + "/" + f,(str(root_path+compressed_folder+"/"+f)))
        print(f, "moved succesfully!")
    elif f.endswith(tuple(app)):
        shutil.move(source + "/" + f,(str(root_path+app_folder+"/"+f)))
        print(f, "moved succesfully!")
    elif f.endswith(tuple(video)):
        shutil.move(source + "/" + f,(str(root_path+video_folder+"/"+f)))
        print(f, "moved succesfully!")
    elif f.endswith(tuple(docs)):
        shutil.move(source + "/" + f,(str(root_path+docs_folder+"/"+f)))
        print(f, "moved succesfully!")
    elif f.endswith(isos):
        shutil.move(source + "/" + f,(str(root_path+isos_folder+"/"+f)))
        print(f, "moved succesfully!")
    elif f.endswith(".srt"):
        shutil.move(source + "/" + f,(str(root_path+subs_folder+"/"+f)))
    elif os.path.isfile(str(source+f)) == True:
        print(f, " file type not recognized, ignored")
print("done!")
