import PIL
from PIL import Image
from tkinter.filedialog import *
import time
from os import system

ts = time.localtime()
fileTimeName = f'{ts[0]}-{ts[1]}-{ts[2]} {ts[3]}-{ts[4]}-{ts[5]}'

def cls():
    try:
        system('cls')
    except:
        system('clear')

def back():
    bak = '\n[1] -> Back to main menu\n[2] -> Exit the Program\n'
    print(bak)
    pilih = input("Select the number: ")
    if pilih.lower() == "back" or pilih == '1':
        cls()
        main()
    elif pilih.lower() == 'exit' or pilih == '2':
        quit()
    else:
        cls()
        print("\nCan't found your selection\n")
        back()

def play():
    print("[!]Prepare for open file folder..")
    time.sleep(3)
    print("[!]Starting opened file...")
    print("[!]Please select your file will you compress...")
    fp = askopenfilename()
    print(f"[!]Get path of the file: \n[{fp}]")
    img = PIL.Image.open(fp)
    width, height = img.size
    print("[!]Start resize image...")
    img = img.resize((width, height), PIL.Image.ANTIALIAS)
    cls()
    print("[+]Your Image has been resized..")
    sav = input("[!]Give file name will you save: ")
    img.save(f'{sav} {fileTimeName}.JPG')
    print(f"[+]File has been saved as [{sav} {fileTimeName}.JPG]...\n")
    back()

def main():
    print("[ Image Compressor ]\n\n[1] -> Start compress an image\n[2] -> Exit the program\n")
    pa = input("Select your number selection: ")
    if pa.lower() == 'start' or pa == '1':
        cls()
        play()
    elif pa.lower() == 'exit' or pa == '2':
        quit()
    else:
        cls()
        print("\n[!]Can't found your selection..\n")
        back()

main()