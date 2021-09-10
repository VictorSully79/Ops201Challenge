# adAdd
# Victor Sullivan
# 20210909
# Script to add user to Active Directory

$Attributes = @{

Enabled = $true
ChangePasswordAtLogon = $true

UserPrincipleName = "ferdi@GlobeXpower.com"
Name = "Franz.Ferdinand"
GivenName = "Franz"
SurName = "Ferdinand"
DisplayName = "Franz Ferdinand"
Description = "TPS Reporting Lead"
Office = "Springfield, OR"

Company = "GlobeX USA"
Department = "TPS"
Title = "TPS Reporting Lead"
City = "Springfield"
State = "Utah"

AccountPassword = "testForAddingPerson" | ConvertTo-SecureString -AsPlainText -Force

}

New-ADUser @Attributes