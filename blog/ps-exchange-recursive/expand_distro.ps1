# Grab a list of Sessions that are currently active
$sessions = Get-PSSession | Select-Object -Property State, Name

# Validate if there is an Exchange Online session already active
$is_online = (@($sessions) -like '@{State=Opened; Name=ExchangeOnlineInternalSession*').Count -gt 0

# If there are no active Exchange Online Sessions, start one!
If ($is_online -ne "True") {
    Connect-ExchangeOnline
}

# This function will expand all of the recipients of any given distribution list
function expand_distro {
    # Grab the parameter (distribution list name)
    $distro = Get-DistributionGroup -Identity $args[0]
    
    # Loop through each member of the distribution list
    $distro_members = Get-DistributionGroupMember -Identity $distro.Identity
    foreach ($member in $distro_members) {
        If ($member.RecipientType -eq "MailUniversalDistributionGroup") {
            # This member is actually another distribution list, 
            # let's recursivelly call the function to further expand the distro
            expand_distro $member.Identity
        } Else {
            # Build a record with the relevant data and
            # Append the member to the result object
            $record = New-Object PSObject -Property @{
                ParentDistro = $distro.PrimarySmtpAddress
                DisplayName = $member.DisplayName
                EmailAddress = $member.PrimarySmtpAddress
            }
            $result.Add($record) | Out-Null
        }
    }
}

# Let's create an ArrayList to hold our results
$result = New-Object System.Collections.ArrayList

# We need to collect the distribution list name from the user
$distro_name = $NULL
While($distro_name -eq $NULL -or 
      $distro_name -eq "") {
    $distro_name = Read-Host -Prompt "Distribution List Email Address"
}

# Set export filename to be the name of the distribution list with a date stamp
$date = Get-Date -Format "yyyyMMdd"
$export_name = $date + "_" + ($distro_name.replace("@", "-").replace(".", "")) + ".csv"

# Call the function with the distribution list name provided
expand_distro $distro_name

# Export the results to our file
$result | Select-Object "EmailAddress", "DisplayName", "ParentDistro" | Sort-Object EmailAddress | Export-Csv -Path $export_name -NoTypeInformation

# Print the file name to the screen
Write-Host "Export file name : $($export_name)" 

