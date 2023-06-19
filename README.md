# omniscient
**ccp spyware for block game**

Omniscient is a program that abuses pinging minecraft servers to anonymously index them. 

How does it work? well, when you ping a minecraft server, it will send back a variety of information such as: description, favicon, player count, ect. The reason a
server does this is that when you open the server menu in minecraft, every saved server will be pinged. Obviously, the server needs to respond with information about
itself to show up on the server list. We can abuse this by randomly generating IP's and then pinging them to see if they are minecraft servers. If they are, then we
save them to a database and send a message to a discord webhook with information about the server for easy reading. This program does exactly that, with a discord bot
included to help go through servers.

Discord webhook example:

![image](https://media.discordapp.net/attachments/467816198592266251/1120217383253053490/image.png)

As you can see, we have the server version, the player count, its location (that's from it's ip), the latency, the favicon, and the description. We send all of this 
information to a discord webhook so that they can be easily picked through for interesting servers.

## servers
You can find the information of every server I've indexed by looking in the "files.txt" file.

## stats
After running this program for like a month on a linux machine lying around, I managed to index **7686** minecraft servers. I ran into 1 youtuber's private server,
along with literally thousands of SMP's. A lot of these servers are just shockbyte subscriptions people forgot to cancel, but rarely, you can stumble into a gem
among the rough.

## limitations
I kinda didn't ever bother adding re-pinging to my program. The idea of re-pinging is to occasionally re-ping servers to gather more detailed information on them.
Randomly generating IP's and pinging them is very intensive, so if you would like to run this, please don't run it on your 2006 Dell All-In-One.

## why????
I saw a video by FitMC on people who made a bot similar to this and subsequently greifed a bunch of 12-year-old's minecraft servers. I maybe might've done a similar
thing and burned like 30 servers to the ground for fun. I made the base of this program in like 3 days and then over time and added more features. I'd love to come
back in the future and add more features to this, but if you really care, go ahead and send a pull request if you've added any new features.

## how do i install this?
Simply install PyCharm Community Edition and load the program, install python 3.9 in the settings menu, and install any package that is required. I'm far too lazy 
to make a requirements.txt file, so have fun. Also, you need to create a CosmosDB in Azure. Then, get all of the values and put them in cosmos.py. Good Luck!
