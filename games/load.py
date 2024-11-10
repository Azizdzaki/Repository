import os
import argparse
import time

def load() -> str:
    parserVar = argparse.ArgumentParser(description="Load")
    parserVar.add_argument("folder_path", nargs="?")
    args = parserVar.parse_args()

    folder_path = args.folder_path

    if not folder_path:                                         
        print("Tidak ada nama folder yang diberikan!")
        print("Usage: python main.py <folder_path>\n")
        exit()
    elif not os.path.isdir(folder_path):                        
        print(f"Folder {folder_path} tidak ditemukan!\n")
        exit()
    else:                                                       
        print("\nLoading...")
        for i in (". . ."):
            print(i)
            time.sleep(0.3)
        owca = """
          ____  _      __ _____  ___ 
         / __ \| | /| / // ___/ /   |
        / /_/ /| |/ |/ // /___ / __ |
        \____/ |__/|__/ \____//_/ |_|                   
        """
        print("Welcome to ..")
        print(owca)
        return folder_path
    return