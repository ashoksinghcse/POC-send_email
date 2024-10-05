from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import parser


def convert_text_from_html(html):
	soup = BeautifulSoup(html, 'html.parser')

	# Extract text from the HTML
	text = soup.get_text()
	return text

def convert_date_from_string(parse_date,format = "YYYY-mm-dd"):
	parse_date = parse_date.split("+")[0].replace(",","")
	print(parse_date)
	#exit()
	#exit()
	return datetime.strptime(parse_date.strip(), "%a %d %b %Y %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")



	return
