# import glob
#
# def search(st):
#     for filename in glob.glob('*.*'):
#         f = open(filename, 'r')
#         content = f.read()
#         if st in content:
#             print(filename)
# search('input')

import glob
import os.path

def search(st, folder):
    for filename in glob.glob(folder+'/*'):
        if os.path.isdir(filename):
            search(st, filename)
        print(os.path.splitext(filename))
        if (".py" in enumerate):
          for i, line in enumerate(open(filename, 'r', encoding='utf-8').readlines()):
                if st in line:
                    print("found in {0} at line {1}, position {2}".format(filename, i+1, line.find(st)+1))

search("input")

