# !! DEPRECATED !!



# High-Octane-Sendit-Spammer
High octane Sendit spammer is coded in python, it is using http post requests making it much faster than my previous spammer coded in python but using selenium

### What is Sendit?
Sendit is a popular snapchat integrated program allowing users to receive anonymous messages from others, it has a web based element where if people put the Sendit link on there snapchat story or send it to someone it allows them to send anonymous messages to the app through the web interface.

## About
The spammer has 3 different options (all compatible with each other)
1. Threaded - makes the process use multiple threads and will ask later how many threads to use (i recommend not going too high as it will work well 50 is a good number but 100 and higher also works).

2. Random sticker - allows you to choose weather to use random stickers (more about stickers later) or the 14 provided stickers.

3. From file - weather or not you want to import the recipient identity(s) from a file if so enable it and the program will make the file ` idlist.csv ` this is were you put your recipient identity(s) newline identifies a separate identity.

## what are stickers and recipient identities?
### Stickers are the headline for the Sendit these are not connected to the specific Sendit so you can make custom ones with custom text even if the recipient didn’t label it that.
### Stickers look like this: 
![sticker](https://user-images.githubusercontent.com/83868916/150907225-f49dfdd3-b3c0-42a1-8ecd-c702026437ff.png)

### Recipient ids are like the persons identifier so that the Sendit api knows where to send-it too.
## How to get recipient ids and sticker ids:
### Open the sendit url on your phone from snapchat and copy it over to your computer (this next part needs to be done on a computer):
![all](https://user-images.githubusercontent.com/83868916/127986071-4a739001-bfdf-4ef5-bf8d-0a5a4ea90f42.png)

### Once you have this url open it in your browser and click ctrl + shift + I and go to the network tab in Inspect
![image](https://user-images.githubusercontent.com/83868916/150907943-4612d4e8-9024-4bce-919d-c1c4c36ad28d.png)

### Now you want to send a sendit can be your own words or click the dice for a random one and once it is sent your network tab should look like this:
![image](https://user-images.githubusercontent.com/83868916/150908226-2a32ed90-a4b1-4fc5-9c81-49858651920a.png)

### Now you want to look at the post requests:
![image](https://user-images.githubusercontent.com/83868916/150908617-c33544da-3f64-4ab2-9172-9518aab7309d.png)

### Click on both of them and then click on the one that has the tab `payload`:
![image](https://user-images.githubusercontent.com/83868916/150908874-031d4eb6-9aa9-4539-8c53-bd7584b16581.png)

### Now you have access to the sticker id and the recipient identity:
![image](https://user-images.githubusercontent.com/83868916/150909414-640b1743-7acf-45da-81bb-693ab84d1ac4.png)

## Compatibility:
This Sendit spammer is compatible with all different Sendit modes eg: kiss marry block, this or that, name for rate.
However it currently only sends normal (if you provide a non normal mode sticker id it will probably break as they require different data values in the json payload).

If I get enough requests for me to add other sticker modes I will but feel free to fork and improve it anyway you want including adding options for other stickers if you want. :)

## Disclaimer:
This program must only be used for educational purpose **only** any malicious use is not condoned by me and I take no responsibility for illegal / unethical use cases.

## Errors:
If you have any errors feel free to open a Issue or contact me on discord `omtoi 101#7794`.

### Also:
Recommended to use threading as it makes it so much faster and so much more efficient.

- Threading 1000 and above seems to completely break sendit while spamming ;)
contacted sendit and the issue on the previous line is now fixed because it was dosing sendits servers, they have now implemented a rate limit 
