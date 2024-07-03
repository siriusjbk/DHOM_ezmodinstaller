# -*- coding: utf-8 -*-
#
# 저작권 (c) 2024 Your Name
#
# 이 소스 코드는 MIT 라이선스에 따라 배포됩니다.
# 자세한 내용은 LICENSE 파일을 참조하십시오.
#
# 소스코드 제목: 예제 프로그램
# 작성자: Your Name
# 작성일: 2024-07-03
#
# 설명:
# 이 프로그램은 Java와 Forge 설치를 관리하는 예제 프로그램입니다.
# 사용자는 프로그램을 통해 Java를 설치하고, 원하는 버전의 Forge를 다운로드 및 설치할 수 있습니다.
# 또한, 프로그램은 Minecraft 모드 파일을 지정된 폴더로 이동시킵니다.
#
# 사용 방법:
# 1. 프로그램을 관리자 권한으로 실행합니다.
# 2. Java 설치 여부를 선택합니다.
# 3. Forge 설치 여부를 선택합니다.
# 4. 모드 파일 이동 여부를 선택합니다.
#

import subprocess
import os
import ctypes
import sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def main():
    if not is_admin():
        print("관리자 권한으로 다시 실행합니다.")
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
        except Exception as e:
            print("권한 상승 요청 실패:", e)
        return

    while True:
        print("Forge를 설치하기 위해서는 Java가 필요합니다.")
        bool_input = input("Java를 설치하시겠습니까? (y/n): ")

        if bool_input.lower() == 'y':
            java_load_f()
            break
        elif bool_input.lower() == 'n':
            break
        else:
            print("소문자 y/n으로만 대답해주십시오.")

    print("Java 프로세스가 종료되었습니다.")
    print("Forge 프로세스를 로드합니다.")

    while True:
        bool_input = input("1.16.5 버전 Forge 36.2.34를 다운로드하시겠습니까? (y/n): ")
        if bool_input.lower() == 'y':
            forge_load_f()
            break
        elif bool_input.lower() == 'n':
            break
        else:
            print("소문자 y/n으로만 대답해주십시오.")

    print("Forge 프로세스가 종료되었습니다.")

    print("모드를 %appdata%의 mods 폴더로 이동시킵니다.")
    print("모드 충돌 방지를 위해 해당 작업을 권장드립니다.")
    print("이동된 모드들은 전부 \n", os.getcwd(), "\n에 저장됩니다.")

    while True:
        bool_input = input("모드를 이동하시겠습니까? (y/n): ")
        if bool_input.lower() == 'y':
            mod_move_f()
            break
        elif bool_input.lower() == 'n':
            break
        else:
            print("소문자 y/n으로만 대답해주십시오.")


def java_load_f():
    java_path = os.path.abspath(r'.\JavaSetup8u411.exe')
    try:
        java_process = subprocess.Popen(java_path)
        java_process.wait()
    except Exception as e:
        print("Java 설치 중 오류가 발생했습니다:", e)


def forge_load_f():
    command = ['java', '-jar', os.path.abspath(r'.\forge-1.16.5-36.2.34-installer.jar')]
    try:
        result = subprocess.run(command, check=True)
        print("프로그램이 종료되었습니다. 종료 코드:", result.returncode)
    except subprocess.CalledProcessError as e:
        print("Forge 설치 중 오류가 발생했습니다:", e)
    except Exception as e:
        print("알 수 없는 오류가 발생했습니다:", e)


def mod_move_f():
    mod_moved_path = os.path.abspath(r'minecraft_mod_folder')
    mod_path = os.path.expandvars(r"%appdata%\\.minecraft\\mods")
    mod_main = os.path.abspath(r"mainmod")

    move_command = f'move /y "{mod_path}\\*.jar" "{mod_moved_path}"'
    copy_command = f'copy /y "{mod_main}\\*.jar" "{mod_path}"'

    try:
        subprocess.run(move_command, shell=True, check=True)
        subprocess.run(copy_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("모드 이동 중 오류가 발생했습니다:", e)
    except Exception as e:
        print("알 수 없는 오류가 발생했습니다:", e)


if __name__ == "__main__":
    print("source code")
    print("https://github.com/siriusjbk/DHOM_ezmodloader/edit/main/README.md")
    main()
    input()