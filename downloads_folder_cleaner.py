import time
import os
from pathlib import Path

def time_stamp():
    t = time.localtime()
    return "{}_{}_{}_{}_{}_{}".format(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)

username = "daniz"

ori_dir = "C:\\Users\\" + username + "\\Downloads"

doc_dir = "C:\\Users\\" + username + "\\Documents"
mus_dir = "C:\\Users\\" + username + "\\Music"
oth_dir = "C:\\Users\\" + username + "\\Others"
pic_dir = "C:\\Users\\" + username + "\\Pictures"
sof_dir = "C:\\Users\\" + username + "\\Software"
vid_dir = "C:\\Users\\" + username + "\\Videos"

doc_ext = {".txt", ".doc", ".pdf", ".odt", ".ods"}
spr_ext = {".csv", ".xls"}
mus_ext = {".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"}
oth_ext = {".rar", ".zip", ".7z"}
pic_ext = {".bmp", ".jpeg", ".jpg", ".png"}
sof_ext = {".exe", ".bat"}
vid_ext = {".avi", ".flv", ".mng", ".mov", ".mp4", ".mpeg", ".mpg", ".qt", ".vob", ".webm", ".wmv", ".3gp"}

dir_ext = [
    (doc_dir, doc_ext),
    (doc_dir, spr_ext),
    (mus_dir, mus_ext),
    (pic_dir, pic_ext),
    (sof_dir, sof_ext),
    (vid_dir, vid_ext)
]

targets = {}

for d, e in dir_ext:
    for ex in e:
        targets[ex] = d

# print (targets)
# os.access(ori_dir, os.R_OK)
# n = os.open
# print (n)
# os.DirEntry
for f in os.scandir(ori_dir):
    if (f.is_file()):
        fn = f.name # File Name
        ldi = fn.rfind(".") # Last Dot Index
        fe = fn[ldi:].lower() # File Extension
        if (fe in targets):
            directory_path = Path(targets[fe])
            directory_path.mkdir(exist_ok=True)
            print ("----")
            print (fn)
            nfn = directory_path.joinpath(fn) # New File Name
            while(nfn.is_file()):
                nfn = directory_path.joinpath("{}_{}{}".format(fn[:fn.rfind(".")], time_stamp(), fn[fn.rfind("."):]))
                time.sleep(1)
            print(nfn)
            # f.rename(directory_path.joinpath(fn)) 
            print ("File {} moved to {}".format(fn, nfn))
            print ("--//--")

# l = list(os.walk(ori_dir))
# for fi in l[0][2]:
#     print(os.path.join(l[0][0], fi))

# for r, d, f in os.walk(ori_dir):
#     for fi in f:
#         print(os.path.join(r, fi))

#     print(r,f)
    # print(os.path.join(r, d))

# for (k, v) in targets:
#     print (k, v)