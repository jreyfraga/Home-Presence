# Home-Presence
Simple Python script that list LAN connected users. Useful for home automation developers (OpenHab, Raspberry, Home Assitant..)

You can use this script to check if someone is at home if his phone is connected to the Wifi for example.

## Requeriments
Of course you need Python and you need to install arp-scan in your system if is not already installed.

In Uuntu/Debian/Raspbian:
```
sudo apt-get install arp-scan
```
## Usage
You need to add to the HomePresence.py file the name of ther users and their MACs in the following line:
```
devices ={'Jhon': "00:00:00:00:00:00",
'Paul': "00:00:00:00:00:00",
'Mary': "00:00:00:00:00:00"}
```
You can add as many users as you want separated by commas.

Then just use:
```
python HomePresence.py
```
If you don't know the MACs of your device you can connected your device to the LAN and execute:
```
arp-scan -l
```
