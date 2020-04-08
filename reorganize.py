import sys
import os
import subprocess
import shutil

#Example path input: /Users/anurag/Downloads/test

def get_arg(index):
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]

def cleanup():
    filelist = []
    for root, dirs, files in os.walk(reorg_dir):
        for name in files:
            filelist.append(root+"/"+name)
    directories = [item[0] for item in os.walk(reorg_dir)]
    for dr in directories:
        matches = [item for item in filelist if dr in item]
        if len(matches) == 0:
            try:
                shutil.rmtree(dr)
            except FileNotFoundError:
                pass
    

if(get_arg(1) == ''):
    print("No path provided.\nUsage: reorganize.py [Path] [-Exclude]")
else:
    if not os.path.exists(sys.argv[1]):
        print("Invalid Path")
        exit()
    reorg_dir = sys.argv[1]



if(get_arg(2) == ''):
    exclude = ()
else:
    exclude = (sys.argv[2])
    
remove_emptyfolders = True

for root, dirs, files in os.walk(reorg_dir):
    for name in files:
        subject = root+"/"+name
        if name.startswith("."):
            extension = ".hidden_files"
        elif not "." in name:
            extension = ".without_extension"
        else:
            extension = name[name.rfind("."):]
        if not extension in exclude:
            new_dir = reorg_dir+"/"+extension[1:]
            if not os.path.exists(new_dir):
                os.mkdir(new_dir)
            n = 1; name_orig = name
            while os.path.exists(new_dir+"/"+name):
                name = "duplicate_"+str(n)+"_"+name_orig
                n = n+1
            newfile = new_dir+"/"+name
            shutil.move(subject, newfile)
            #shutil.copy(subject, newfile)

if remove_emptyfolders != False:
    cleanup()

print("\nCompleted")    

