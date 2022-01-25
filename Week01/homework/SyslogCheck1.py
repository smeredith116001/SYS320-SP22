#Credit To Duane Duston 

# Create and interfaced to search through syslog files
import re, sys

def _syslog(filename,listOfKeywords):
    # Open a file
    with open(filename) as f:
            #read in the file and save it to a variable
                        contents = f.readlines()

#Lists to store the results
    results = []
    
# Loop through the list returned. Each element is a line from the Linux2k file
    for line in contents:
            # Loops through the keywords
            for eachKeyword in listOfKeywords:
                        # If the 'line' contains the keyword then it will print
                        # If eachhkeyword is line:
                        # Searches and returns results using a regualr expression search
                        x = re.findall(''+eachKeyword+'', line)
                          
                        for found in x:
                            results.append(found)
    # Check to see if there are results
    if len(results) == 0:
        print("No Results")
        sys.exit(1)
    #Sort the list
    results = sorted(results)

    return results
                   
                                         


    


       
        
            

            

            
       
      

        