# Create and interfaced to search through syslog files
import yaml, re ,sys, csv

# Open the yaml file


    

def _logs(filename,service):
    
    with open('searchTerms.yaml', 'r') as yf:
        keywords = yaml.safe_load(yf)
    
    #Query the yaml file for the 'term' or direction and 
    #retrieve the strings to search on
    keywordLib= keywords[service]
    listOfKeywords = []
    items = keywordLib.items()
    for item in items:
        listOfKeywords.append(items[1])
    # Open a file
    with open(filename) as f:
    #Indentation Reader Change
    #Reads the file
        contents = csv.reader(f)
        #Populates content
    
    
#keywords = ['sshd\(pam_unix\)\[[0-9]{3,8}\]: authentication failure;', 'session opened for user','exited abnormally']

#print(contents)
#Lists to store the results
    results = []
    
# Loop through the list returned. Each element is a line from the smallSyslog file
    for line in contents:
            # Loops through the keywords
            for eachKeyword in listOfKeywords:
                        # If the 'line' contains the keyword then it will print
                        # If eachhkeyword is line:
                        # Searches and returns results using a regualr expression search
                        x = re.findall(r''+ eachKeyword + '', line [1])
                        # print(x)    
                        for found in x:
                            results.append(found)
    # Check to see if there are results
    if len(results) == 0:
        pass
    #Sort the list
    results = sorted(results)

    return results
                   
                                         


    


       
            
            # Append the returned keywords to the results list 
            

            

            
       
      

        