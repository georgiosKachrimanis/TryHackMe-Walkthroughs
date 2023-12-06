# About:
Metasploit is the most widely used exploitation framework. Metasploit is a powerful tool that can support all phases of a penetration testing engagement, from information gathering to post-exploitation.
![Alt text](</Media/Metaspolit/img_01.jpg>)

As per usual my walkthroughs will not explain the content of the room. Also, will not give you the answers directly but the tips you need to find the answers.

# Task 1. Introduction to Metasploit
Start the Machine and the Attack Box. 

# Task 2. Main Components of Metasploit

### What is the name of the code taking advantage of a flaw on the target system?
You can find the answer on the top of the Task. 
Read on the clarification of the recurring concepts.

### What is the name of the code that runs on the target system to achieve the attacker's goal?
Again, you can can find the answer on the top of the Task. 
Read on the clarification of the recurring concepts.

### What are self-contained payloads called?
You can find the answer in the Payloads section.

### Is "windows/x64/pingback_reverse_tcp" among singles or staged payload?

Again, You can find the answer in the Payloads section.<br> 
*\*Tip use the exact wording they use for the question(singles, staged)*

# Task 3. Msfconsole

### How would you search for a module related to Apache?
You can find the answer in the Search section.<br>
*\*Tip: Search function can use many arguments and is really fast*

### Who provided the auxiliary/scanner/ssh/ssh_login module?

Just use the `info` as the Hint is suggesting.<br>
`info auxiliary/scanner/ssh/ssh_login`

# Task 4. Working with modules

### How would you set the LPORT value to 6666?

You can use the command `set`. 


### How would you set the global value for RHOSTS  to 10.10.19.23 ?

You can use the command `setg`.


### What command would you use to clear a set payload?

You can use the command `unset`.

### What command do you use to proceed with the exploitation phase?

You can use the command `exploit`

