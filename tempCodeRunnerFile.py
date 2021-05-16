import os

# Get .txt files
for f_name in os.listdir('D:\Introduction'):
    if f_name.endswith('.txt'):
        print(f_name)