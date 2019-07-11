import os
files=os.listdir("/home/ganapathi/PycharmProjects/userpro")
for file in files:
    f=(file.split('.'))[0]
    print(f)
