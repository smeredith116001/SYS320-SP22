# Create and interfaced to search through syslog files
import re, sys, yaml

# Open the yaml file
try:
    with open('searchTerms.yaml', 'r') as yf:
        keywords = yaml.safe_load(yf)
except EnvironmentError as e:
    print(e.strerror)
    

def _logs(filename,service, term):
    #Query the yaml file for the 'term' or direction and 
    #retrieve the strings to search on
    terms = keywords[service][term]
    
    listOfKeywords = terms.split(",")
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
        print("No Results")
        sys.exit(1)
    #Sort the list
    results = sorted(results)

    return results
                   
                                         


    


       
            
            # Append the returned keywords to the results list 
            

            

            
       
      

        