# Create and interfaced to search through syslog files
import yaml, re, sys

# Open the yaml file


def _logs(filename,service):
    with open('searchTerms.yaml', 'r') as yf:
        contents = yaml.safe_load_all(yf)

        #Query the yaml file for the 'term' or direction and 
        #retrieve the strings to search on
        #keywordLib= keywords[service]
        #Loops through the yaml file and retrieves the documents
        for keyVal in contents:
            #print (keyVal)
            #Retrieves each of the items for each service 
            for key, value in keyVal[service].items():
                        listOfKeywords = []
                        items = keyVal.items()


<<<<<<< HEAD

        for item in items:
            listOfKeywords.append(items[1])
=======
    items = keyVal.items()
    listOfKeywords = []
    for item in items:
        
        listOfKeywords.append(items[1])
>>>>>>> 860dfa97febec72eddebd76a9038600e8b9c3476
    # Open a file
    with open(filename) as f:
            #read in the file and save it to a variable
            contents = f.readlines()

    
    
    
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
                        x = re.findall(''+eachKeyword+'', line)
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
            

            

            
       
      

        