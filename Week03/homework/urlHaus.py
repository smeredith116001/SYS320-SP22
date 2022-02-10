
#import re 
#This part Imports the nesscary libarys to run these lines
import re,csv
# Replaced the 1 with an L, Spacing
#Function that will be called in main, that defines the name of the file and SearchTerm
def urlHausOpen(filename, searchTerm):
    
    #Indentation, Took out the '' swui
    #Opens the file
    with open(filename) as f:
    #Indentation Reader Change
    #Reads the file
        contents = csv.reader(f)
        #Populates contents
        for _ in range(9):
             #Indentation 
            next(contents)
            
       
    #Indentation Exchanged the for loops
    #Looks through each line in Contacts
        for eachLine in contents:
            #Indentation 
            #Looks for keywords in those lines
            for keyword in searchTerm:
                #Indentation removed the , removed spacing added the ''
                #Puts those values equal to x
                x = re.findall(r''+keyword+'',eachLine[2])
                #Indentation 
                #Loop for x
            for _ in x:
                #Indentation 
                #Removes the TT so programs dont convert 
                the_url = eachLine[2].replace("http","hxxp")
                #Indentation changed to line 7
                the_src = eachLine[7]
                #Fixed spcacing, put in the period 
#prints out the results
                print("""
                URL: {}
                Info: {}
                {}""".format(the_url, the_src, "*" * 60))

    #Indentation 
    
    






#for keyword in searchTerms:
#for eachLine in contents:
#x = re.findall(r+keyword+,eachLine[2])
#for _ in x:
# Don't edit this line. It is here to show how it is possible
# to remove the "tt" so programs don't convert the malicious
# domains to links that an be accidentally clicked on.
#the_url = eachLine[2].replace("http","hxxp")
#the_src = eachLine[4]
#print("""
#URL:
#Info: 
#{}""",format(the_url, the_src,"*"+60))