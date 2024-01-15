#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import sys

if len(sys.argv) < 3:
	print("Usage: fetch-beecrowd [id] [output-file]")
	exit(-1)

number = int(sys.argv[1])
output_file = sys.argv[2]
response = requests.get(f"https://www.beecrowd.com.br/repository/UOJ_{number}.html", headers={'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.1 Chrome/59.0.3017.125 Safari/537.36'})
if response.status_code != 200:
	print("Error getting page of the given id")
	print(response.status_code)
	exit(-1)

html = BeautifulSoup(response.content, 'html.parser')
text = "\n".join([el.text.strip('\n') for el in html.select('.division > p')])
if(text == '\n' or text == ''):
	print("[!] Sem entrada")
with open(output_file, "w") as file:
	file.write(text)
