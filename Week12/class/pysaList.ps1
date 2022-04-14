# List the files in a directory and 
#Get-ChildItem -recurse -Include *.docx,*.pdf,*.txt -Path .\Documents |Select FullName
Get-ChildItem -recurse -Include *.docx,*.pdf,*.txt -Path .\Documents | export-csv `
-Path files.csv

# Import CSV file.
$fileList = import-csv -Path .\files.csv -header FullName

# Loop through the results
foreach($f in $fileList){

    Get-ChildItem -Path $f.FullName
}
