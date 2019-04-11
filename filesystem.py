import os, glob

os.chdir("/Users/daesy13/Sites/Demos/Python-Interview")
for file in glob.glob("*.jpg"):
    print(file)

#small program that uses os module and glob module
#goes into a specific directory and print out all jpg files