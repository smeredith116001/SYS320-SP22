Copy-Item "C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe" -Destination "C:\Users\Sebby"

Rename-Item -Path "C:\Users\Sebby\powershell.exe" -NewName "XpOm-431.exe"
$file = "C:\Users\Sebby\XpOm-431.exe"
If (Test-Path $file)
{
    Write-Host "File is found"
}
Else 
{
    Write-Host "Error file not found"
}


Add-Content -Path 'C:\Users\Sebby\Readme.READ' -Value 'If you want your files restored, please contact me at dunston@champlain.edu. I look forward to doing business with you.'

#Set-Location 'C:\Users\Sebby' $sbText

#Tests the file
$ReadMe = "C:\Users\Sebby\Readme.READ"
If (Test-Path $ReadMe) 
{
    Write-Host "File is found"

}
Else 
{
    Write-Host "Error file not found"
}


