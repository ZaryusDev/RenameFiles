import os

chemainEdit = r"C:\Users\zimin\Pictures\Amis\2022 - Sorties"

files = os.listdir(chemainEdit)

count = 1

for file in files:
    extension = file.split('.')[-1]
    fileName = str(count).zfill(3)
    count += 1
    os.rename(chemainEdit+"\\"+file, chemainEdit+"\\"+fileName+"."+extension)