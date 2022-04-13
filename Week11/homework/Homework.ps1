while ($True) {
    New-SSHSession -ComputerName '192.168.6.71' -Credential (Get-Credential sebastian.meredith) -Port 2222
    # Add a prompt to run commands 
    $var = Read-host -Prompt "Please enter Windows or IPTables"
    (Invoke-SSHCommand -index 0 $var).Output
    switch($var)
    {
    
    "Windows"{
        
        break
    }
    
        
     #$var{
        #"Windows"
        #break
    # }
     
    "IPTables"{
         $pro = Read-Host -Prompt "How many ips"
         foreach($u in $pro)
            {
         
             
             $temp = Read-Host -Prompt "Enter the IP"
             Add-Content -Path "C:\Users\Sebby\ips-tables.txt" -Value $temp 
            
            }
            break
     }
     
    }
    
    # Run command on remote SSH server
    
}
# Extract the IP Addresses
$regex_drop = '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\.\b'

#Append the IP addresses to the temporary IP lost.
Select-String -path "C:\Users\Sebby\ips-tables.txt" -Pattern $regex_drop | `
ForEach-Object { $_.Matches} | `
ForEach-Object { $_.Value} | Sort-Object | Get-Unique | `
Add-Content -FilePath "C:\Users\Sebby\ips-tables.txt"
# Get the IP addresses discovered, loop through and replace the begining of the line with the IPTables syntax
# After the IP address, add the remaining IPTables syntax and save the results to a file 
# iptables -A INPUT -s 108.191.2.72 -j DROP
(Get-Content -Path "C:\Users\Sebby\ips-tables.txt") | % `
{ $_ -replace "^"," iptables -A INPUT -s" -replace "$", "-j DROP"} | `
Out-File -FilePath "C:\Users\Sebby\ips-tables2.bash"

Set-SCPItem -ComputerName '192.168.6.71' -Credential (Get-Credential sebastian.meredith) -Port 2222 -RemotePath '/home/sys320' -LocalFile '.\ips-tables.txt'