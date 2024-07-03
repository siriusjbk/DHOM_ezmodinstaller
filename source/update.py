import os
import shutil

def move_jar_files(src_folder, dst_folder):
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    for filename in os.listdir(src_folder):
        if filename.endswith(".jar"):
            shutil.move(os.path.join(src_folder, filename), os.path.join(dst_folder, filename))

if __name__ == "__main__":
    update_folder = "update"
    mod_folder = os.path.expandvars(r"%appdata%\.minecraft\mods")
    move_jar_files(update_folder, mod_folder)
    print("모든 .jar 파일이 이동되었습니다.")
    input()
