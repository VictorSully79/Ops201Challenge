$ServerList = Get-ADComputer -Filter * -Properties OperatingSystem, DnsHostName | Where OperationgSystem -Like "*Server*" | Select DnsHostName
$MasterList = @()
foreach ($Server in $ServerList) {
    $MyObject = New-Object PSObject -Property @{
        ServerName = $Server.DnsHostName
        OS = (Get-CimInstance -ComputerName $Server.DnsHostName -ClassName Win32_OperatingSystem).Caption
        RAM = (Invoke-Command $Server.DnsHostName {(systeminfo | Select-String 'Total Physical Memory:').ToString().split(':'[1].Trim()})
        CFreeGB = (Invoke-Command $Server.DnsHostName {(Get-WmiObject win32_logicaldisk -Filter "DeviceID='C:'").FreeSpace / 1gb -as [int]})
        CTotalGB = (Invoke-Command $Server.DnsHostName {(Get-WmiObject win32_logicaldisk -Filter "DeviceID='C:'").Size / 1gb -as [int]})
    }
    $MasterList += $MyObject
}
$MasterList | Select ServerName, OS, RAM, CTotalGB, CFreeGB |
Export-csv C:\Users\$env:username\Desktop\ServerOverview.csv -NoTypeInformation -Encoding Unicode