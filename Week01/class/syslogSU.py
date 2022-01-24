import SyslogCheck
import importlib
importlib.reload(SyslogCheck)


def su_open(filename, searchTerms):
    
    is_found = SyslogCheck._syslog(filename,searchTerms)
    # Found List
    found = []
    #Looping through
    for eachFound in is_found:
        #Split the results
        sp_results = eachFound.split(" ")
        # Appending the results
        found.append(sp_results[5])
        
    # Print  
    returnedValues = set(found)
    
    for eachValue in returnedValues:
        
        print(eachValue)
        
    

   
    
    
                    
                     
                     
        
        
   

 
        

        

                                   

    
    