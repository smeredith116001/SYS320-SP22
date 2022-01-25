#Credit To Duane Duston
import SyslogCheck1
import importlib
importlib.reload(SyslogCheck1)


def ssh_auth(filename, searchTerms):
    
    is_found = SyslogCheck1._syslog(filename,searchTerms)
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
        
    

   
    
    
                    
                     
                     
        
        
   

 
        

        

                                   

    
    