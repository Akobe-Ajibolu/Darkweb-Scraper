#!/usr/bin/env python3

from requests_tor import RequestsTor
from bs4 import BeautifulSoup
import time
import argparse

parser = argparse.ArgumentParser(description="This is a darkweb scraping/monitoring tool")
parser.add_argument("-c", "--change_ip", dest="change_ip", action="store_true", help="Change Tor/Public IP address")
def get_sites(links):
	website_titles = []
	for link in links:
		title = link.get('title')
		website_titles.append(title)

	return website_titles


def print_sites(website_titles):
	for website_title in website_titles:
		if website_title is not None:
			print(f"\t {website_title}")


def get_new_ip():
	print("[-].	Generating new Tor IP this will take a minute or two")
	rt.new_id()
	time.sleep(30)
	

rt = RequestsTor(tor_ports=(9050,), tor_cport=9051)
headers = {
    "Origin": "https://www.foxnews.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }

args = parser.parse_args()
if args.change_ip:
	get_new_ip()

ip_address = rt.check_ip()

print(f"[-].	Accessing the deep web with {ip_address}")
print("[+].	Companies Currently listed by lockbit:")
url = "http://lockbit7z2jwcskxpbokpemdxmltipntwlkmidcll2qirbu7ykg46eyd.onion/"
request = rt.get(url, headers=headers)
html_content = request.text
soup = BeautifulSoup(html_content, 'html.parser') 
links = soup.find_all('a')
website_titles = get_sites(links)
print_sites(website_titles)


