
<img src="Media/Benign/Benign_0.jpg" height=100% width=100% >

<h1>About</h1>

Welcome to another one of my walkthroughs. 

Before you start this CTF is good to have finished the rooms  [splunk101](https://tryhackme.com/room/splunk101) and [splunk201](https://tryhackme.com/room/splunk201).

# Start Here

You first need to start the VM machine that is hosting Splunk and,  

<img src="Media/Investigating with Splunk/splunk_1.jpg" height=30% width=30% >

if you are using the VM that are provided by TryHackMe.

<img src="Media/Investigating with Splunk/splunk_2.jpg" height=50% width=50% >

Also for your own convenience you can use a separate tab for the AttackBox by doing the following:

1. Click on the View in full screen at the bottom left of the AttackBox screen.
<img src="Media/Investigating with Splunk/splunk_3.jpg" height=50% width=50% >

2. Now a new tab will open with the VM and you can close the split screen by clicking on exit split view. You now have 2 tabs one with the questions and one with the VM.
    <img src="Media/Investigating with Splunk/splunk_4.jpg" height=50% width=50% >

3. Next step is to use as filter the win_eventlogs with the command `index=win_eventlogs`. Change the time range for now to `All time`and the mode to `Verbose Mode`.

<img src="Media/Benign/Benign_1.jpg" height=100% width=100% >


# Task 2, Scenario: Identify and Investigate an Infected Host

### How many logs are ingested from the month of March, 2022?

We need to change the time range for March of 2022:

<img src="Media/Benign/Benign_2.jpg" height=50% width=50% >

Then just use the total number of events.

<img src="Media/Benign/Benign_3.jpg" height=50% width=50% >


### Imposter Alert: There seems to be an imposter account observed in the logs, what is the name of that user?

This is not so hard to find.

First of all we will find the username on the left panel.
When we click on it we see 10 only names but as you can see the total number of users is 11. 
We can click on the Top Values and a new report will be created.
<img src="Media/Benign/Benign_4.jpg" height=50% width=50% >

Now we open the Statistics Tab and we can see all the names. You can see that one more name is at the end of the list a bit different than the correct one. `Amelia VS Amel1a`

<img src="Media/Benign/Benign_5.jpg" height=50% width=50% >


### Which user from the HR department was observed to be running scheduled tasks?

The scheduled tasks on Windows are using the `schtasks.exe` so if we use it in the filter we get 4 usernames as results. Only one is from HR

<img src="Media/Benign/Benign_6.jpg" height=50% width=50% >

### Which user from the HR department executed a system process (LOLBIN) to download a payload from a file-sharing host.

Now we will use the filter to check all the users from HR what process are running.

<img src="Media/Benign/Benign_7.jpg" height=50% width=50% >

We Click on the CommandLine and then on Rare Values.


<img src="Media/Benign/Benign_8.jpg" height=50% width=50% >

Now we can see a Certutil.exe is one of the binaries we can find also in the Repository we get as a tip.

<img src="Media/Benign/Benign_9.jpg" height=50% width=50% >

Now we can use the name of this executable to see who and when this event happened.

<img src="Media/Benign/Benign_10.jpg" height=50% width=50% >


### To bypass the security controls, which system process (lolbin) was used to download a payload from the internet?

We already know the name from the previous steps.


### What was the date that this binary was executed by the infected host? format (YYYY-MM-DD)

We can find the date from the time this one event was created.

<img src="Media/Benign/Benign_11.jpg" height=50% width=50% >


### Which third-party site was accessed to download the malicious payload?

Again we can find the information by the details of the event.

<img src="Media/Benign/Benign_12.jpg" height=50% width=50% >


### What is the name of the file that was saved on the host machine from the C2 server during the post-exploitation phase?

Yes you guessed it correct ... you can find the information in the details of the event.

<img src="Media/Benign/Benign_13.jpg" height=50% width=50% >

### The suspicious file downloaded from the C2 server contained malicious content with the pattern THM{..........}; what is that pattern?

Let's connect to the download server and find out. You can also find the answer to the last question in the same image.

<img src="Media/Benign/Benign_14.jpg" height=50% width=50% >
 
### What is the URL that the infected host connected to?

See the previous image.

<h2>This is the end of another CTF, hope you enjoyed it and if you have any comments please feel free to contact me.</h2>