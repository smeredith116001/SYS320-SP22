$drop_urls = @('https://rules.emergingthreats.net/blockrules/emerging-botcc.rules','https://rules.emergingthreats.net/blockrules/compromised-ips.txt')
$var = Read-host -Prompt "Please enter Windows or IPTables"
switch ($var) {
     "Windows" {
         
        # Extract the filename
        $temp = $drop_urls[0].split("/")

        # The last element in the array plucked off is the filename
        $file_name = $temp[-1]

        if (Test-Path $file_name) {

            continue
        } else {
            # Download the rules list
            Invoke-WebRequest -Uri $u -OutFile $file_name

        }

        $input_path = ".\emerging-botcc.rules"

        # Extract the IP addresses
        # 108.190.109.107
        # 108.191.2.72
        $regex_drop = '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

        # Append the Ip addresses to the temporary IP list
        Select-String -Path $input_path -Pattern $regex_drop | `
        ForEach-Object { $_.Matches } | `
        ForEach-Object { $_.Value } | Sort-Object | Get-Unique | `
        Out-File -FilePath ".\emerging-botcc.tmp"

        # Get the IP addresses discovered, loop through and replace the beginning of the line with teh IPTables syntax
        # After the IP address, add the remaining IPTables syntax and save the results to a file
        # iptables -A INPUT -s 108.191.2.72 -j DROP
        (Get-Content -Path ".\emerging-botcc.tmp") | % `
        { $_ -replace "^","iptables -A INPUT -s " -replace "$", "-j DROP" } | `
        Out-File -FilePath "emerging-botcc.bash"

        Set-SCPItem -ComputerName '192.168.6.71' -Credential (Get-Credential sebastian.meredith) -Port 2222 `
        -Destination 'C:\Users\Sebby' -Path 'emerging-botcc.bash'

      }
     "IPTables" {
         
        # Extract the filename
        $temp = $drop_urls[1].split("/")

        # The last element in the array plucked off is the filename
        $file_name = $temp[-1]

        if (Test-Path $file_name) {

            continue
        } else {
            # Download the rules list
            Invoke-WebRequest -Uri $u -OutFile $file_name

        }

        $input_path = ".\compromised-ips.txt"

        $regex_drop = '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

        # Append the Ip addresses to the temporary IP list
        Select-String -Path $input_path -Pattern $regex_drop | `
        ForEach-Object { $_.Matches } | `
        ForEach-Object { $_.Value } | Sort-Object | Get-Unique | `
        Out-File -FilePath ".\compromised-ips.tmp"

        # Get the IP addresses discovered, loop through and replace the beginning of the line with teh IPTables syntax
        # After the IP address, add the remaining IPTables syntax and save the results to a file
        # iptables -A INPUT -s 108.191.2.72 -j DROP
        (Get-Content -Path ".\compromised-ips.tmp") | % `
        { $_ -replace "^","iptables -A INPUT -s " -replace "$", "-j DROP" } | `
        Out-File -FilePath "compromised-ips.bash"

        Set-SCPItem -ComputerName '192.168.6.71' -Credential (Get-Credential sebastian.meredith) -Port 2222 `
        -Destination 'C:\Users\Sebby' -Path 'compromised-ips.bash'

      }
 }

Set-SCPItem -ComputerName '192.168.6.71' -Credential (Get-Credential sebastian.meredith) -Port 2222 -RemotePath '/home/sys320' -LocalFile '.\ips-tables.txt'