# High-Octone-Sendit-Spammer
High octane Sendit spammer is coded in python, it is using http post requests making it much faster than my previous spammer coded in python but using selenium

### What is Sendit?
Sendit is a popular snapchat integrated program allowing users to recieve anonymous messages from others, it has a web based element where if people put the Sendit link on there snapchat story or send it to someone it allows them to send anonymous messages to the app through the web interface.

## About
The spammer has 3 different options (all compatible with eachother)
1. threaded - makes the process use multiple threads and will ask later how many threads to use (i reckomend not going too high as it will work well 50 is a good number but 100 and higher also works).

2. random sticker - allows you to choose weather to use random stickers (more about stickers later) or the 14 provided stickers.

3. from file - weather or not you want to import the recipient identity(s) from a file if so enable it and the program will make the file ` idlist.csv ` this is were you put your recipient identity(s) newline identifys a seperate identity.

## what are stickers and recipient identitys?
### Stickers are the headline for the Sendit these are not connected to the specific Sendit so you can make custom ones with custom text even if the recipient didnt label it that.
### stickers look like this: 
![sticker](https://user-images.githubusercontent.com/83868916/150907225-f49dfdd3-b3c0-42a1-8ecd-c702026437ff.png)

### Recipient ids are like the persons identifier so that the Sendit api knows were to send-it too.
## how to get recipient ids and sticker ids.
open the sendit url on your phone from snapchat:
