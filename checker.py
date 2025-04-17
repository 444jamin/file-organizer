import os

folder = '/mnt/c/Users/Lenovo/Desktop/Pictures'

with os.scandir(folder) as entries:
    for entry in entries:
        print(entry.name)