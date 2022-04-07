#Login to a remote SSH server
#New-SSHSession -ComputerName '192.168.6.71' -Credential (Get-Credential sebastian.meredith) -Port 2222

while ($True) {

    # Add a prompt to run commands 
    $the_cmd = read-host -Prompt "Please enter a command"
    # Run command on remote SSH server
    (Invoke-SSHCommand -index 0 $the_cmd).Output
}

Set-SCPItem -ComputerName '192.168.6.71' -Credential (Get-Credential sebastian.meredith) -Port 2222 -RemotePath '/home/sys320' -LocalFile '.\Proof.png'