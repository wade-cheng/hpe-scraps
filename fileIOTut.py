import os
path = 'files\\problem01'
files = os.listdir(path)
for item in files:
    if os.path.isfile(os.path.join(path,item)):
        print(f'{item} is a file')
    elif os.path.isdir(os.path.join(path,item)):
        print(f'{item} is a directory')
    else:
        print(f'{item} is something else')
