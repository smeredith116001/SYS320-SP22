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

def statFile(toStat):

    #i is going to be the varible used for each of the metadata elements
    i = os.stat(toStat,follow_symlinks=False)
    mode = i[0]
    #inode
    inode=i[1]
    # uid
    uid = i[4]
    # gid
    gid = i[5]
    #file size 
    fsize = i[6]
    #access time
    atime = i[7]
    # modification time
    mtime = i[9]
    # ctime => windows is the birth of the file, when it was created
    # unix it is when attritbutes 
    ctime = i[9]
    crtime = i[9]

    print("*0|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(toStat,inode, mode,uid, gid, fsize, atime, mtime, ctime ,crtime))
for eachFile in fList:

    statFile(eachFile)
    