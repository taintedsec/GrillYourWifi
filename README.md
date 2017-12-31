# GrillYourWifi
*Mass Access Point Network Deauthentication Attack Tool*

Built With:
> [Python2.7](https://www.python.org)
> [Aircrack-ng](https://www.aircrack-ng.org)

Compatible Operating Systems:
> [Kali Linux i686](https://offensive-security.com)
> [Ubuntu Linux 16.04 LTS](https://ubuntu.com)

## Description

The **GrillYourWifi** network deauthentication tool is a script that allows mass *Denial of Service* attacks on remote Access Points with beacon requests that are in range of the host network interface card that is actively configured for *monitor mode*

## Warning

This network attack tool can be used for _malicious use_, and *the developers of this script are not responsible for any damage caused* by the innapropriate usage of `grillyourwifi.py` 

## Instructions (Usage)

_Requrirements_:
- Python2.7 [https://python.org](https://www.python.org)
- Aircrack-ng [https://aircrack-ng.com](https://www.aircrack-ng.org)
- Pip - Python package installer [https://pip.pypa.io/en/stable/](https://pip.pypa.io/en/stable/)

*_Installation_*:
1. `pip install pandas` or `apt-get install python-pip`
2. `cd /root/Documents/`
3. `git clone https://github.com/taintedsec/GrillYourWifi.git`
4. `cd GrillYourWifi`
5. `touch targets.txt target_vector.txt`
6. `python2 grillyourwifi.py`

## Technical Details

The python script `grillyourwifi.py` parses standard out from `airodump-ng [interface]`and sets the interval write-to limit to 1 second, and stores the BSSID column into a list object, which is iterated over until EOF. `grillyourwifi.py` proceeds to spoof the network interface card to the corresponding mac address of the target BSSID AP and injects 10 deauthentication frames into the remote access point to disrupt the WPA 4-way handshake. For more technical details of the _WiFi Deauthentication Attack_ see also [https://en.wikipedia.org/wiki/Wi-Fi_deauthentication_attack](https://en.wikipedia.org/wiki/Wi-Fi_deauthentication_attack)
