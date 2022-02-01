import logCheck
import importlib
importlib.reload(logCheck)


def proxy_events1(filename, service, term):
    
    is_found = logCheck._logs(filename,service,term)
    # Found List
    found = []
    #Looping through
    for eachFound in is_found:
        #Split the results
        sp_results = eachFound.split(" ")
        # Appending the results
        #GET /cgi-bin/welcome HTTP/1.1" 404 435
        found.append(sp_results[0]+ " " + sp_results[2] + "opened with proxy")
        
    # Print  
    getValues = set(found)
    
    for eachValue in getValues:
        
        print(eachValue)
        
    

   
    
    
                    
                     
                     
        
        
   

 
        

        

                                   

    
    