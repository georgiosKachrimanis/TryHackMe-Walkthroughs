<img src="Photos/img_0.png" >
# About

This is a guide for [Wireshark: Packet Operations room in TryHackMe](https://tryhackme.com/room/wiresharkpacketoperations). The room is visible by free users but is only really usable by subscribers (you will have to use the VM in order to complete it).
Also, I strongly suggest to finish the first room [Wireshark: The Basics](https://tryhackme.com/room/wiresharkthebasics)

# General Info

There are a lot of build in filters that are really helpful in all situations using Wireshark. For example one of the most useful is Name Resolution.

Lets see one example:
<img src="Photos/img_1.png" >

On this pcap file you can see the Source and Destination IPs as numbers. 
Using the Resolve Network Address filter <br>
(View->Name Resolution -> Resolve Network Address) <br>
we can see that some of the IPs are transformed and show us the Domain name.

<img src="Photos/img_2.png" >

Now if you use the Resolve Transport Address (View->Name Resolution -> Resolve Transport Address) we can see extra information in the info about ports etc. 

<img src="Photos/img_31.png" >

**As I mentioned these filters are really useful and try to remember them in general especially if you are planing to try some Wireshark CTF**

# Task 1 
You just need to click Start Machine <img src="Photos/img_3.png" >

Also, after this click on Show Split View
<img src="Photos/img_4.png" >

This will split your screen in half.  
<img src="Photos/img_5.png" >

If you are lucky and have a big monitor this is not a problem. If you are using a smaller monitor or laptop then the best thing you can do is to go at the bottom of the VM part of the screen and press the View in full screen button.

<img src="Photos/img_6.png" width="30%" height="25%">

After that a new browser tab will open with only the VM showing

<img src="Photos/img_7.png" >

Now you can go back at the tab with the split screen and close the VM on this tab. 

<img src="Photos/img_8.png" width="30%" height="25%">

Now you will have two tabs one with the questions/examples and one tab with the VM you are going to use for the testing / answering.

# Task 2

In this task we going to learn about the Statistics tab and the useful tools that are available to us.<br>During the explanation you can see the tips of how to use the statistics tab.<br>I will not explain any of these the author of this room does a much better job than me.<br>So lets jump directly to the questions of this Task.<br><br>In total there are 5 questions.<br><br>
*I hope you can understand that I am not going to tell you how you can run Wireshark or how to open a file* 

## Question 1  
**Investigate the resolved addresses. What is the IP address of the hostname starts with "bbc"?**

Using the tools that this room wants to teach us we should do the following:<br>
1. Statistics --> Resolved addresses.<br>
    <img src="Photos/img_2.0.png" width="40%" height="40%">
2. You click on the drop down menu of "All entries", and you choose "Host".<br>
    <img src="Photos/img_21.png" width="30%" height="30%"><br>
3. Then on the search entry you type "bbc" and then you will get the hostname that starts with bbc.     
    <img src="Photos/img_22.png" width="30%" height="30%"> 

## Question 2
**What is the number of IPv4 conversations?**

Using the tools that this room wants to teach us we should do the following:<br>
1. Statistics --> Conversations.<br>On the window that will pop-up you can see the total amount of connections:
    <img src="Photos/img_23.png" width="40%" height="40%">

## Question 3
**How many bytes (k) were transferred from the "Micro-St" MAC address?**

Using the tools that this room wants to teach us we should do the following:<br>
1. Statistics --> Endpoints.
2. Stay on the Ethernet tab.
3. Click on the Name Resolution.
4. You can now see the answer to the question.

<img src="Photos/img_24.png" width="40%" height="40%">

## Question 4
**What is the number of IP addresses linked with "Kansas City"?**

Using the tools that this room wants to teach us we should do the following:<br>
1. Statistics --> Endpoints.
2. Open the IPv4 Tab.
3. You can now count the Endpoint connections originating from Kansas City.

<img src="Photos/img_25.png" width="40%" height="40%">

## Question 5
**Which IP address is linked with "Blicnet" AS Organization?**

Using the tools that this room wants to teach us we should do the following:<br>
1. Statistics --> Endpoints.
2. Open the IPv4 Tab.
3. Click on the AS Number so the list will be Alphabetically sorted based on the As Company names. Search for Blicnet.

<img src="Photos/img_26.png" width="40%" height="40%">


