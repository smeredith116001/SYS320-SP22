
#import re 
import re,csv
# Replaced the 1 with an L, Spacing
def urlHausOpen(filename, searchTerm):
    
    #Indentation, Took out the '' swui
    with open(filename) as f:
    #Indentation Reader Change
        contents = csv.reader(f)
        for _ in range(9):
             #Indentation 
            next(contents)
            
       
    #Indentation Exchanged the for loops
        for eachLine in contents:
            #Indentation 
            for keyword in searchTerm:
                #Indentation removed the , removed spacing added the ''
                x = re.findall(r''+keyword+'',eachLine[2])
                #Indentation 
            for _ in x:
                #Indentation 
                the_url = eachLine[2].replace("http","hxxp")
                #Indentation changed to line 7
                the_src = eachLine[7]
                #Fixed spcacing, put in the period 
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