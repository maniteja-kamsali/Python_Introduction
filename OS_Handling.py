import os
entries = os.listdir('D:\Introduction')
print(entries)

import os

with os.scandir('D:\Introduction') as entries:
    for entry in entries:
        print(entry.name)

import os

# List all files in a directory using os.listdir
basepath = 'D:\Introduction'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)

import os

# Get .txt files
for f_name in os.listdir('D:\Introduction'):
    if f_name.endswith('.txt'):
        print(f_name)

# Python program to explain os.path.join() method
	
# importing os module
import os

# Path
path = r"C:\Users\MANI\PycharmProjects\Desktop"

# Join various path components
print(os.path.join(path,  "Resume_MANI_TEJA.pdf"))
