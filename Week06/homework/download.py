# File to traverse a given directory andf it's subdirs and retrieve all the files
import os, argparse

# parser
parser = argparse.ArgumentParser(
    description="Traverses a directory and builds a forensic body file",
    epilog="Developed by Sebastian Meredith, 20200210"
)
# Add arguements to pass to the fs.py program
parser.add_argument("-d","--directory", required="True", help ="Directory that you want to traverse.")
# Parse the arguments
args = parser.parse_args()

rootdir = args.directory
# Get infomation from the commandline
#print(sys,argv)
#Directory to traverse
#rootdir = sys.argv[1]

#print(rootdir)
fList=[]
# In our story, we will traverse a directory

# Check if this argument is a directory
if not os.path.isdir(rootdir):
    print("Invalid directory => {}" .format(rootdir))
    exit()
# Crawl through the provided directory
for root, subfolders, filenames in os.walk(rootdir):

    for f in filenames:
        fileList = root + "/" + f
        fList.append(fileList)
#print(fileList)

