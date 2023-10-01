<img src="Media/Investigating with Splunk/splunk_0.jpg" >

<h1>About</h1>

Welcome to another one of my walkthroughs.

Before you start this CTF is good to have finished the rooms  [splunk101](https://tryhackme.com/room/splunk101) and [splunk201](https://tryhackme.com/room/splunk201).

# Start Here

You first need to start the VM machine that is hosting Splunk and if you are using the VM that are provided by TryHackMe.

<img src="Media/Investigating with Splunk/splunk_1.jpg" height=50% width=50% >

<img src="Media/Investigating with Splunk/splunk_2.jpg" height=50% width=50% >

<<<<<<< HEAD
Also for your own convenience you can use a separate tab for the AttackBox by doing the following:
=======
Also for your own convenience you can use a seperate tab for the AttackBox by doing the following:
>>>>>>> c109d764ac94066d866325fe8f034ac090c5568c

1. Click on the View in full screen at the bottom left of the AttackBox screen.

    <img src="Media/Investigating with Splunk/splunk_3.jpg" height=50% width=50% >

2. Now a new tab will open with the VM and you can close the split screen by clicking on exit split view. You now have 2 tabs one with the questions and one with the VM.
    
    <img src="Media/Investigating with Splunk/splunk_4.jpg" height=50% width=50% >

3. When the machines are running you just press the search button.
    
    <img src="Media/Investigating with Splunk/splunk_5.jpg" height=50% width=50% >
4. Now you must type where the ingested logs are `index="main"`
   
    <img src="Media/Investigating with Splunk/splunk_6.jpg" height=50% width=50% >

<h2> Answers </h2>

### How many events were collected and Ingested in the index main?

You will just need to filter the search time frame to All time. Then the answer is the total amount of events.

<img src="Media/Investigating with Splunk/splunk_7.jpg" height=50% width=50% >

### On one of the infected hosts, the adversary was successful in creating a backdoor user. What is the new username?

With some help of google you can search which EvenID is used when a Windows account is created. Just to help you out is `EventID="4720"`. If we use it as a search parameters we get the following.

<img src="Media/Investigating with Splunk/splunk_11.jpg" height=50% width=50% >

Just pay attention that the name is using leek.

### On the same host, a registry key was also updated regarding the new backdoor user. What is the full path of that registry key?

With some help of google you can search which EvenID is used when a RegistryKey is updated. Just to help you out is `EventID="13"`. We already know the user so we can use both of them as search parameters.

<img src="Media/Investigating with Splunk/splunk_9.jpg" height=50% width=50% >
<img src="Media/Investigating with Splunk/splunk_10.jpg" height=50% width=50% >

### Examine the logs and identify the user that the adversary was trying to impersonate.

Just leave only the basic filter `index="main"` You can click on the interesting fields --> Users. Then you will see a name that looks a lot like the name of question 1.

 <img src="Media/Investigating with Splunk/splunk_8.jpg" height=50% width=50% >

### What is the command used to add a backdoor user from a remote computer?

Now, Windows is always adds a log with EventId="1" for every new command that is being executed. So by adding this in the filter we get about 19 returned processes. On the left panel you can find the CommandLine if you click on it and read the commands you can find out the one we are looking for.

<img src="Media/Investigating with Splunk/splunk_12.jpg" height=50% width=50% >

### How many times was the login attempt from the backdoor user observed during the investigation?

Just use the user name on the filter `User=A1berto`. Then you can find out how many times he tried to login.

<img src="Media/Investigating with Splunk/splunk_13.jpg" height=50% width=50% >

### What is the name of the infected host on which suspicious Powershell commands were executed?

Add as filter powershell, you can find it on the 1st event of the list.

<img src="Media/Investigating with Splunk/splunk_14.jpg" height=50% width=50% >


### PowerShell logging is enabled on this device. How many events were logged for the malicious PowerShell execution?
Searching again we find that the EventID for PowerShell Operational Log for Command Invocation is 4103. We use it as a filter and then we get the result we are looking for.


<img src="Media/Investigating with Splunk/splunk_15.jpg" height=50% width=50% >

### An encoded Powershell script from the infected host initiated a web request. What is the full URL?

Now this is a hard one, 1st you need to Decode the Base64 string you can find in the event we were looking for before.

I used [CyberChef](https://gchq.github.io/CyberChef/), for the 1st decoding but it is obfuscated and we will have to make some analytical digging.

<img src="Media/Investigating with Splunk/splunk_16.jpg" height=50% width=50% >

As you can see CyberChef is not really easy to read so I used a basic text editor to help me out. There is again a Base64 string and when we use again CyberChef FromBase64 IP : http:10.10.10.5 then we can now add the /news.php we see in the text. 

<img src="Media/Investigating with Splunk/splunk_17.jpg" height=50% width=50% >

Next stop is to Defang this in CyberChef. In the Process use everything otherwise you will not have the correct answer for the last question.


<img src="Media/Investigating with Splunk/splunk_18.jpg" height=50% width=50% >

You can see the answer to the last question at the Output.


<h2>Congratulations</h2>

If you have any suggestions please feel free to contact me.
