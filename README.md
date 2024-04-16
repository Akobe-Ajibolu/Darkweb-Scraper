# Darkweb scraper

## Important Note:

- This script is intended for educational purposes only and should not be used for malicious activities.

## Ethical Web Scraping for Security Research

This script demonstrates potential techniques for security researchers to gather information on compromised organizations from publicly available sources on the darkweb (Lockbit). It's crucial to prioritize ethical data collection practices.

## Functionality:

- Automate the process of checking for organizations compromised by Lockbit.
- Tor IP Rotation: Includes an optional function `-c, --change_ip` to change the researcher's Tor exit node IP address with each script execution, potentially enhancing anonymity.

## Target Audience:

Security professionals who want to learn about potential methods for threat intelligence gathering (within legal and ethical boundaries).

## Future Enhancements:

Explore incorporating data from additional publicly available sources/forums on the dark web.

## Usage
### Requirements.
- This script is built for linux based OS. 
**- Install Tor**.
```
sudo apt install tor
```
**- Edit torrc using any editor of choice** `sudo nano /etc/tor/torrc`
	- Uncomment `Controlport 9051`
	- Uncommenting `CookieAuthentication` and change it value from `1` to `0`.
**- Restart tor**:
```
sudo service tor restart
```
**- Install python modules.**
```
pip3 install requests-tor
pip3 install bs4
pip3 install argparse
```

### Run script

```
python3 dark_web_scraper.py
```

Check help menu using `--help`

> [!IMPORTANT]
> Credit to whom credit is due - this script was inspired by John Hammond's Scraping Dark Web Sites wwith Python video.
