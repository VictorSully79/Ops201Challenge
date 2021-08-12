# Ops-201 Challenges

### I do not have a favorite here. There is a lot of power in scripting.  Finding the intricacies in the way Bash and PowerShell function are subtle but important.  I enjoy finding the correct syntax and will go over all of the scripts I have written so far and try for the same outcome in both languages. 

### Scripting and automation are incredibly important.  Saving both time and money as well as freeing up resources for other tasks.  I look forward to improving my knowledge of cmdlets and piping.  These two things are essential for pulling the information you want in a useful manner. 


## 20210727

## Ops Challenge: Class 02

### Objectives

1. Stores a fetches network adapter information, then saves that information to a variable.
2. Generates a output.txt file containing the network adapter information.

### [Network Adapter](networkAdapter.sh)

## 20210728

## Ops Challenge: Class 03

### Objectives

1. Write a Bash script that prints the login history of users on this computer.

2. Your script must use at least one function and one variable.

### Stretch Goal

1. Include a function that accepts a parameter and uses it.

### [Bash Login](bashLogin.sh)

## Ops Challenge: Class 04

### Objectives - Arrays

1. Write a Bash script that:

- Creates four directories: dir1, dir2, dir3, dir4

- Put the four directories in an array

- References the array variable to create a new .txt file in each directory

### [Bash Arrays](bashArrays.sh)

## 20210730

## Ops Challenge: Class 05

### Objectives - Loops

1. Write a script that displays running processes, asks the user for a PID, then kills the process with that PID.

2. Use a loop in your script.

### [Bash Loop](bashLoop.sh)

## 20210802

## Ops Challenge: Class 06

### Objectives - Conditionals

1. Create a Bash script that detects if a file or directory exists, then creates it if it does not exist.

2. Your script must use at least one list, one loop, and one conditional.

### [Conditionals](conditionals.sh)

## Ops Challenge: Class 07

### Uses lshw to display system information to the screen about the following components:

Name of the computer:
- CPU
  - Product
  - Vendor
  - Physical ID
  - Bus info
  - Width
- RAM
  - Description
  - Physical ID
  - Size
- Display adapter
  - Description
  - Product
  - Vendor
  - Physical ID
  - Bus info
  - Width
  - Clock
  - Capabilities
  - Configuration
  - Resources
  - Network adapter
  - Description
  - Product
  - Vendor
  - Physical ID
  - Bus info
  - Logical name
  - Version
  - Serial
  - Size
  - Capacity
  - Width
  - Clock
  - Capabilities
  - Configuration
  - Resources

### [System Information](systemInformation.sh)

## Ops Challenge: Class 09

### Objective

Create a Powershell script that fetches useful System event logs.

### [Event Logs](eventLogs.ps1)

## 20210806

## Ops Challenge: Class 10

### Objective

Create a Powershell script that performs these operations on separate lines. The overall script is not designed to operate holistically, but rather act as a reference for how to execute various interesting operations with the process family of Powershell commandlets. Clearly indicate with comments each component below.

- Print to the terminal screen all active processes ordered by highest CPU time consumption at the top.
- Print to the terminal screen all active processes ordered by highest Process Identification Number at the top.
- Print to the terminal screen the top five active processes ordered by highest Working Set (WS(K)) at the top.
- Start the process Internet Explorer (iexplore.exe) and have it open https://owasp.org/www-project-top-ten/.
- Start the process Internet Explorer (iexplore.exe) ten times using a for loop. Have each instance open https://owasp.org/www-project-top-ten/.
- Close all Internet Explorer windows.
- Kill a process by its Process Identification Number. Choose a process whose termination won’t destabilize the system, such as Internet Explorer or MS Edge.

### [System Process Commands](systemProcessCommands.ps1)

## 20210809

## Ops Challenge: Class 11

### Objective

Write a Powershell script that automates the configuration of a new Windows 10 endpoint. Your script should perform the following:

- Enable File and Printer Sharing
- Allow ICMP traffic
- Enable Remote management
- Remove bloatware
- Enable Hyper-V
- Disable SMBv1, an insecure protocol

### [Automated Endpoints](automatedEndpoint.ps1)

## 20210810

## Ops Challenge: Class 12

### Objective 

Create a Powershell script that performs the following operations:

- Create a local file called network_report.txt that holds the contents of an ipconfig /all command.
- Use Select-String to search network_report.txt and return only the IP version 4 address.
- Remove the network_report.txt when you are finished searching it.
  
### [PowerShell IP Analysis](powerShellIP.ps1)

## 20210811

## Ops Challenge: Class 13

### Objective

- Create a bash script that asks a user to type a domain, then displays information about the typed domain. Operations that must be used include:
  - whois
  - dig
  - host
  - nslookup

### [Bash Domain Analyzer](bashDomainAnalyzer.sh)

 
 ### More Pages
- [Ops-201 Course Outline](ops-201.md)
- [Back to Readme](README.md)  
  