# Create an interface to search through syslog files
import re, sys, yaml, csv

# Open the Yaml file


def _logs(filename,service):
    
    with open('searchTerms.yaml', 'r') as yf:
        keywords = yaml.safe_load(yf)


    # Query the yaml file for the 'term' or direction and
    # retrieve the strings to search on
    keywordDict = keywords[service]

    # listOfKeywords = terms.split(",")

    # Splits each key-value pair from keywordDict and appends to listOfKeywords
    listOfKeywords = []
    items = keywordDict.items()
    for item in items:
        #print(item)
        listOfKeywords.append(item[1])

    # Open a file
    with open(filename) as f:

        # read in the file and save it to a variable
        contents = csv.reader(f)

        # Lists to store results
        results = []

        # loop through the list returned. Each element is a line from the log file
        for line in contents:
            #print(line)
            #Loops through the keywords
            for eachKeyword in listOfKeywords:

            # searches returned results using regex
                x = re.findall(r'' + eachKeyword + '', line[1])

                for found in x:
                    # Append the returned keywords to the results list
                    results.append(found)
                #print(eachKeyword)
        # Check to see if there are results
        if len(results) == 0:
            pass

        # Sort the list
        results = sorted(results)
        #print(results)

        return results
                # print(x)                 


    


       
            
            # Append the returned keywords to the results list 
            

            

            
       
      

        