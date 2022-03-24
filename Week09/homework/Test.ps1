# Get a list of running processes
# Get a list of members

# Get-Process | get-member

# Get a list of processes: name, id, path
#Get-process | Select-object ProcessName , id, path | Export-csv -Path `
#C:\Users\Sebby\Desktop\processes.csv

# System Services and properties
# Get-Service | Get-Member
#Get-service | select-object Status, Name, DisplayName, BinaryPathName |export-csv -Path $outputName

# Varibles
$outputName = "C:\Users\Sebby\Desktop\runningServices.csv"
$outputName1 = "C:\Users\Sebby\Desktop\runningServices.csv1"



# Get a list of running services
Get-service | Where-Object { $_.Status -eq "Running"} |export-csv -Path $outputName

# Check to see if the file exists

if ( Test-path $outputName1 ) {

    write-host -backgroundcolor "Green" -foregroundcolor "white" "Service file was created!"
}
    else {
    write-host -backgroundcolor "red" -foregroundcolor "white" "Service file was not created!"
}