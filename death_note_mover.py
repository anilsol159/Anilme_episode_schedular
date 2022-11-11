import os
import shutil


START_PATH = "D://Movies//Death Note//"
DESTINATION = r"C:\Users\Anil\Desktop\To Watch"



files = os.listdir(START_PATH)
if len(files)==0:
    print("You are all caught up!")
    input()
elif len(files)==1:

    first_num = int(files[0].split()[4])

    file_name = f"[AnimeFlix.in] Death Note Ep {str(first_num).zfill(2)} 1080p BD Dual Audio HEVC [ZeUs].mkv"
    first_file_path = START_PATH + file_name
    shutil.move(first_file_path,DESTINATION)

else:
    first_num = int(files[0].split()[4])

    file_name = f"[AnimeFlix.in] Death Note Ep {str(first_num).zfill(2)} 1080p BD Dual Audio HEVC [ZeUs].mkv"
    first_file_path = START_PATH + file_name
    shutil.move(first_file_path,DESTINATION)
    s_file_name = f"[AnimeFlix.in] Death Note Ep {str(first_num+1).zfill(2)} 1080p BD Dual Audio HEVC [ZeUs].mkv"
    s_file_path = START_PATH + s_file_name
    shutil.move(s_file_path,DESTINATION)