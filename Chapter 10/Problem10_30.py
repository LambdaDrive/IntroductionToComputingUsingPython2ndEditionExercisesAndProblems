import os
def traverse(pathname, d):
    for dirpath, dirs, files in os.walk(pathname):
        for filename in files:
            fname = os.path.join(dirpath, filename)
            space = fname.count('/')
            print(' ' * space,fname)