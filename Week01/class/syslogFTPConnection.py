import SyslogCheck
import importlib
importlib.reload(SyslogCheck)


def ftp_connection(filename, searchTerms):
    
    is_found = SyslogCheck._syslog(filename,searchTerms)
    # Found List
    found = []
    #Looping through
    for eachFound in is_found:
        #Split the results
        sp_results = eachFound.split(" ")
        # Appending the results
        found.append(sp_results[3])
        
    # Print  
    hosts = set(found)
    
    for eachHost in hosts:
        
        print(eachHost)
        
    

   
    
    
                    
                     
                     
        
        
   

 
        

        

                                   

    
    