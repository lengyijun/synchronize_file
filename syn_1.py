__author__ = 'steven'
#同步两个文件的脚本
#python3.5编译

import os
import shutil
import sys

#注意\会转义，所以要在转义一次
source_file=["C:\\Users\\steven\\Desktop\\test1.txt",
             "C:\\synchronous\\static\\Bookmarks"]
target_file=["C:\\Users\\steven\\Desktop\\test2.txt",
             "C:\\Users\\steven\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Bookmarks"]

def main():
    global source_file
    global target_file

    for i in range (len(source_file)):
        if (not os.path.isfile(source_file[i]) and not os.path.isfile(target_file[i])):
            print("both "+source_file[i]+" and "+target_file[i]+" don't exist")
            print("nothing done")

        elif (not os.path.isfile(source_file[i])):
            f=open(source_file[i],'a')
            f.close()
            shutil.copy2(target_file[i],source_file[i])
            print("change "+source_file[i]+" to "+target_file[i])

        elif (not os.path.isfile(target_file[i])):
            f=open(target_file,'a')
            f.close()
            shutil.copy2(source_file[i],target_file)
            print("change "+target_file[i]+" to "+source_file[i])

        else:
            source_file_time=round(os.stat(source_file[i]).st_mtime,0)
            target_file_time=round(os.stat(target_file[i]).st_mtime,0)

            print (source_file[i]+" "+str(source_file_time))
            print (target_file[i]+" "+str(target_file_time))

            if(source_file_time>target_file_time):
                f=open(target_file[i]+'_backup',"w")
                f.close()
                shutil.copy2(target_file[i],target_file[i]+'_backup')
                shutil.copy2(source_file[i],target_file[i])
                print("change "+target_file[i]+" to "+source_file[i])
            else:
                f=open(source_file[i]+'_backup',"w")
                f.close()
                shutil.copy2(source_file[i],source_file[i]+'_backup')
                shutil.copy2(target_file[i],source_file[i])
                print("change "+source_file[i]+" to "+target_file[i])


main()

